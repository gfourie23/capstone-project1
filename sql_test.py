import psycopg2
import openai
import app

openai.api_key = app.config['OPENAI_API_KEY']

conn = psycopg2.connect(
    database="schedule_app",
)

cursor = conn.cursor()


#Fetch patient preferences from the database
cursor.execute("SELECT name, frequency, timeframe_start, timeframe_end, preferred_days, preferred_times FROM patients;")
rows = cursor.fetchall()


cursor.close()
conn.close()

prompt = f"Act as an appointment scheduler for a doctor using the following patient information. The patient's name {rows[0]} the frequency {rows[1]} of visits allowed per week, and the patient's preferred_days {rows[3]} of the week and preferred_times {rows[4]} of the day. Patients can only have one appointment in a day and appointments are one hour long. Create a schedule that accommodates the patient preferences, does not overlap in time, and lists weekly visits according to the frequency of visits allowed in a week."


response = openai.Completion.create(
    engine="gpt-3.5-turbo",
    promp=prompt,
    max_tokens=200
)

schedule = response['choices'][0]['text']

print(schedule)


"""prompt = f"Act as a therapy appointment scheduler. I will give you the following patient information: name {rows[0]}, the frequency{rows[1]} of visits allowed per week, the timeframe {row[2]} of dates that the sessions occur, and the patient's preferred_days {rows[3]} of the week and preferred_times {rows[4]} of the day. A patient can only have one visit in a day and usually will have one or two days in between their therapy visits. The therapy visits are 45 mins and need a 15 minute break in between. You need to return a schedule with suggested times for each patient that do not overlap or exceed the patient's weekly frequency within the respective timeframes. Show me the results in time slots that I can put in my calendar including dates."""
