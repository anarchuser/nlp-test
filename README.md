# NotepadAI - Backend

Python server for the NotepadAI project.

## About NotepadAI
Semesterproject SS2019 - [CODE University of Applied Sciences](https://code.berlin/en/)

##### How might we...
support students in taking the most out of a lecture?

To achieve this we are building a mobile app using Flutter which records a lecture, transcripts it and helps the student summarize it.

## Purpose
This is the backend corresponding to the [NotepadAI App](https://gitlab.com/julian.bertsch42/notepadai_app).
It listens to the NotepadAI App and receives an audio stream from the microphone of the smartphone running said app.

#### Process
1) Wait for a phone to connect
2) Receive the audio stream
3) Remove noise from the stream
4) Transcript the stream into multiple seperate sentences
5) Send the text stream back to the client
