

"""@app.route('/create-schedule')
def generate_schedule():

    patient_info = Patient.query.all()
    for patient in patient_info:

        messages = [
            {"role": "system", 
            "content": "Act as an appointment scheduler for a clinician using the following patient information: Name: {patient.name} Frequency: {patient.frequency} Timeframe: {patient.timeframe_start} to {patient.timeframe_end} Preferred Days: {', '.join(patient.preferred_days)} Preferred Times: {', '.join(patient.preferred_times)}}" },
            {"role": "user", 
            "content": "Schedule [Frequency] one-hour therapy appointments for [Patient Name] within the specified timeframe. Ensure that appointments are distributed throughout the week on their preferred days and times. Adjust the schedule to accommodate any constraints and preferences."}],


    response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=200
        )
 

    if 'choices' in response and response['choices']:
        schedule = response.choices[0].message.content
        print(json(schedule))
    else:
        print(f"Error from OpenAI API: {response}")"""





"""conn = psycopg2.connect(
    database="schedule_app",
)

cursor = conn.cursor()


#Fetch patient preferences from the database
cursor.execute("SELECT name, frequency, timeframe, preferred_days, preferred_times FROM patients;")
rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
conn.close()

prompt = f" Act as a therapy appointment scheduler. I will give you the following patient information: {name}, the {patient.frequency} of visits allowed per week, the {timeframe} of dates that the sessions occur, and the patient's {preferred_days} of the week and {preferred_time} of the day. A patient can only have one visit in a day and usually will have one or two days in between their therapy visits. The therapy visits are 45 mins and need a 15 minute break in between. You need to return a schedule with suggested times for each patient that do not overlap or exceed the patient's weekly frequency within the respective timeframes. Show me the results in time slots that I can put in my calendar including dates."""

"""response = client.chat.completion.create(
    model="gpt-3",
    prompt=prompt,
    max_tokens=200
)"""


#################### GOOOGLE CALENDAR API #######################

# Recurring events

"""event = {
  'summary': 'Appointment',
  'location': 'Somewhere',
  'start': {
    'dateTime': '2011-06-03T10:00:00.000-07:00',
    'timeZone': 'America/Los_Angeles'
  },
  'end': {
    'dateTime': '2011-06-03T10:25:00.000-07:00',
    'timeZone': 'America/Los_Angeles'
  },
  'recurrence': [
    'RRULE:FREQ=WEEKLY;UNTIL=20110701T170000Z',
  ],
  'attendees': [
    {
      'email': 'attendeeEmail',
      # Other attendee's data...
    },
    # ...
  ],
}

recurring_event = service.events().insert(calendarId='primary', body=event).execute()

print recurring_event['id']"""


"""event = {
  'summary': 'Google I/O 2015',
  'location': '800 Howard St., San Francisco, CA 94103',
  'description': 'A chance to hear more about Google\'s developer products.',
  'start': {
    'dateTime': '2015-05-28T09:00:00-07:00',
    'timeZone': 'America/Los_Angeles',
  },
  'end': {
    'dateTime': '2015-05-28T17:00:00-07:00',
    'timeZone': 'America/Los_Angeles',
  },
  'recurrence': [
    'RRULE:FREQ=DAILY;COUNT=2'
  ],
  'attendees': [
    {'email': 'lpage@example.com'},
    {'email': 'sbrin@example.com'},
  ],
  'reminders': {
    'useDefault': False,
    'overrides': [
      {'method': 'email', 'minutes': 24 * 60},
      {'method': 'popup', 'minutes': 10},
    ],
  },
}

event = service.events().insert(calendarId='primary', body=event).execute()
print 'Event created: %s' % (event.get('htmlLink'))"""

'''{"role": "system", "content":"Act as an appointment scheduler for a clinician using the following patient information."},
    {"role": "user", "content": "The patient's name {patient.name} the frequency {row[1]} of visits allowed per week, and the patient's preferred_days {row[3]} of the week and preferred_times {row[4]} of the day. Patients can only have one appointment in a day and appointments are one hour long. Create a schedule that accommodates the patients' preferences, does not overlap in time, and lists weekly visits according to the frequency of visits allowed in a week. Here are the patients information: {row}"}]'''



#@app.route('/edit-pt/<int:patient_id>', methods=["GET"])
# def generate_schedule(patient_id):
    #Query patient information from the database
"""patient_info = Patient.query.get(patient_id)
    for patient in patient_info

    #Prompt openai to create schedule
response = client.chat.completions.create(
        model="gpt-3.5-turbo",
       
        messages=[
        {"role": "system", "content": "Act as an appointment scheduler for a clinician using the following patient information: Name: {patient.name} Frequency: {patient.frequency} Timeframe: {patient.timeframe_start} to {patient.timeframe_end} Preferred Days: {patient.preferred_days} Preferred Times: {patient.preferred_times}}" },
        {"role": "user", "content": "Schedule [Frequency] one-hour therapy appointments for [Patient Name] within the specified timeframe. Ensure that appointments are distributed throughout the week on their preferred days and times. Adjust the schedule to accommodate any constraints and preferences."}],
        max_tokens=200
    )
schedule = response.choices[0].message.content

print(schedule)"""

 """return jsonify(schedule)"""

   """# Construct the prompt using patient_data
    messages = f"Based on the provided patient information, let's schedule {patient_data[1]} one-hour therapy appointments per week for {patient_data[0]}. " \
         f"The timeframe for the appointments is from {patient_data[2]} to {patient_data[3]}. " \
         f"To accommodate the patient's preferred days and times, I will consider their preferred days: {patient_data[4]} and preferred times: {patient_data[5]}. " \
         f"Here is the schedule for the appointments:\n"

    # Iterate through preferred days and times and create the schedule
    for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
        schedule_entries = []
        for time_slot in patient_data[5].strip('{}').split(','):
            schedule_entries.append(f"{patient_data[0]} - {time_slot}")
        day_schedule = f"{day}: {', '.join(schedule_entries)};"
        messages += f"{day_schedule}\n"""
    
    """system_message = {
        "role": "system", 
        "content": "Act as an appointment scheduler for a clinician using the following patient information: Name: {patient_data[0]} Frequency: {patient_data[1]} Timeframe: {patient_data[2]} to {patient_data[3]} Preferred Days: {patient_data[4]} Preferred Times: {patient_data[5]}}",
    }

    user_message = {
        "role": "user", 
        "content": "Schedule {patient_data[1]} one-hour therapy appointments per week for {patient_data[0]} within the specified timeframe. Ensure that appointments are distributed throughout the week on their preferred days and times. Adjust the schedule to accommodate any constraints and preferences. Format the schedule with the names of the patients and start times for the appointments for each day.",
    }

    messages.extend([system_message, user_message])"""


########### Deleted from app. ####

################# OPENAI API call########################
    
conn = psycopg2.connect(
    database="schedule_app",
)
cursor = conn.cursor()

#Fetch patient preferences from the database
patient_information = cursor.execute("SELECT name, frequency, timeframe_start, timeframe_end, preferred_days, preferred_times FROM patients;")
data = cursor.fetchall()

messages = []

#for patient_data in data:
    #name, frequency, timeframe_start, timeframe_end, preferred_days, preferred_times = patient_data
    #print(patient_data)
    #print(data)
    #print(patient_data[0])
    

# Add system message
system_message = {
    "role": "system",
    "content": "Act as an appointment scheduler for a clinician using the following patient information."
}
messages.append(system_message)

# Add user message for each patient
for patient_data in data:
    user_message = {
        "role": "user",
        "content": f"Schedule {patient_data[1]} one-hour therapy appointments per week for {patient_data[0]}. " \
                   f"The timeframe for the appointments is from {patient_data[2]} to {patient_data[3]}. " \
                   f"To accommodate the patient's preferred days and times, consider their preferred days: {patient_data[4]} " \
                   f"and preferred times: {patient_data[5]}. Ensure that appointments do not overlap with exisiting appointments."
                    f"Return the schedule in a format suitable for Google Calendar API:\n" \
                   f"event = {{'{patient_data[0]}'\n" \
                   f"  'summary': '{patient_data[0]}',\n" \
                   f"  'location': 'Your Location',\n" \
                   f"  'description': 'Therapy appointment with {patient_data[0]}',\n" \
                   f"  'start': {{\n" \
                   f"    'dateTime': '2023-12-06T07:00:00-08:00',  # Replace with actual start time\n" \
                   f"    'timeZone': 'America/Denver',\n" \
                   f"  }},\n" \
                   f"  'end': {{\n" \
                   f"    'dateTime': '2023-12-06T08:00:00-08:00',   # Replace with actual end time\n" \
                   f"    'timeZone': 'America/Denver',\n" \
                   f"  }},\n" \
                   f"  'recurrence': ['RRULE:FREQ=WEEKLY;COUNT='{patient_data[1]}'],\n" \
                   f"}}"
    }
    messages.append(user_message)


cursor.close()
conn.close()




"""response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=messages,
    max_tokens=200
)

print(response.choices[0].message.content)"""