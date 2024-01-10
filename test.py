
import os 
import unittest
from flask import Flask, render_template
from app import app, Patient, NewPatientForm, PatientEditForm, db

class TestCalendarRoute(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_show_cal_route(self):
        response = self.app.get('/calendar')
        self.assertEqual(response.status_code, 200)  
        self.assertIn(b'Show calendar', response.data)  
        self.assertIn(b'homepage.html', response.data)  

class TestPatientListRoute(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL")
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_show_pt_list_route(self):
        # Insert a sample patient for testing
        sample_patient = Patient(name='John Doe')
        db.session.add(sample_patient)
        db.session.commit()

        response = self.app.get('/pt-list')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'John Doe', response.data)

class TestAddPatientFormRoute(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL")
                app.config['WTF_CSRF_ENABLED'] = False 
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_add_pt_form_valid_submission(self):
        # Simulate a form submission
        data = {
            'name': 'John Doe',
            'address': '123 Main St',
            'city': 'Cityville',
            'frequency': 'daily',
            'timeframe_start': '01/01/2024',
            'timeframe_end': '03/01/2024',
        }

        response = self.app.post('/add-pt', data=data, follow_redirects=True)

        self.assertEqual(response.status_code, 200)  # 
        self.assertIn(b'John Doe', response.data)  

        patient = Patient.query.filter_by(name='John Doe').first()
        self.assertIsNotNone(patient) 

    def test_add_pt_form_invalid_submission(self):
    
        data = {}

        response = self.app.post('/add-pt', data=data, follow_redirects=True)

        self.assertEqual(response.status_code, 200)  # 
        self.assertIn(b'Add new patient information', response.data)  

        patient = Patient.query.filter_by(name='John Doe').first()
        self.assertIsNone(patient)

class TestEditPatientFormRoute(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL")
        app.config['WTF_CSRF_ENABLED'] = False 
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_edit_patient_form_valid_submission(self):
        # Create a sample patient for testing
        sample_patient = Patient(name='John Doe', address='123 Main St', city='Cityville', frequency='daily', timeframe_start='01/01/2024', timeframe_end='03/01/2024')
        db.session.add(sample_patient)
        db.session.commit()

        # Simulate a valid form submission
        data = {
            'name': 'Updated Name',
            'address': 'Updated Address',
            'city': 'Updated City',
            'frequency': 'weekly',
            'timeframe_start': '01/10/2024',
            'timeframe_end': '03/10/2024',
            'preferred_days': ['Monday', 'Wednesday'],
            'preferred_times': ['1pm-3pm'],
        }

        response = self.app.post(f'/edit-pt/{sample_patient.id}', data=data, follow_redirects=True)

        self.assertEqual(response.status_code, 200) 
        self.assertIn(b'Updated Name', response.data)  

        
        updated_patient = Patient.query.filter_by(name='Updated Name').first()
        self.assertIsNotNone(updated_patient) 

    def test_edit_patient_form_invalid_submission(self):
        # Create a sample patient for testing
        sample_patient = Patient(name='John Doe', address='123 Main St', city='Cityville', frequency='daily', timeframe_start='01/10/2024', timeframe_end='03/10/2024')
        db.session.add(sample_patient)
        db.session.commit()

        # Simulate an invalid form submission (missing required fields)
        data = {}

        response = self.app.post(f'/edit-pt/{sample_patient.id}', data=data, follow_redirects=True)

        self.assertEqual(response.status_code, 200)  
        self.assertIn(b'Edit existing patient information', response.data)  

        not_updated_patient = Patient.query.filter_by(name='John Doe').first()
        self.assertIsNotNone(not_updated_patient)


class TestDeletePatientRoute(unittest.TestCase):

     def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL")

        app.config['WTF_CSRF_ENABLED'] = False 
        self.app = app.test_client()
        db.create_all()

     def tearDown(self):
        db.session.remove()
        db.drop_all()

        sample_patient = Patient(name='John Doe', address='123 Main St', city='Cityville', frequency='daily', timeframe_start='01/01/2024', timeframe_end='03/01/2024')
        db.session.add(sample_patient)
        db.session.commit()

        response = self.app.post(f'/pt-list/{sample_patient.id}/delete', follow_redirects=True)

        self.assertEqual(response.status_code, 200)  # 
        self.assertIn(b'John Doe has been deleted successfully.', response.data)

        # Check if the patient is deleted from the database
        deleted_patient = Patient.query.filter_by(name='John Doe').first()
        self.assertIsNone(deleted_patient)  

     def test_delete_patient_route_invalid_deletion(self):
        # Simulate attempting to delete a non-existent patient
        response = self.app.post('/pt-list/999/delete', follow_redirects=True)

        self.assertEqual(response.status_code, 404)  
        self.assertIn(b'Not Found', response.data)  

        
        existing_patient = Patient.query.first()
        self.assertIsNone(existing_patient)


if __name__ == '__main__':
    unittest.main()
