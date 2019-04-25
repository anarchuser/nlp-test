# HypNote - Backend
#### Branch: transcript-gcloud
----

Python server for the HypNote project

Semesterproject SS2019 - [CODE University of Applied Sciences](https://code.berlin/en/)

### About the project
##### Problem
We focused on the following question:

```How might we support students in taking the most out of a lecture?```

##### Solution
To help students listening to lectures while being able to take notes, we want to provide a mobile application which eases up on the part of taking notes.

So, our goal is to provide an app which automatically transcripts a lecture while giving the student the opportunity to mark and edit the transcript on the fly.

It listens to the [HypNote App](https://gitlab.com/julian.bertsch42/notepadai_app) and receives an audio stream from the microphone of the smartphone running said app.
This stream is then send to the Google Cloud Speech API, which returns a stream of transcripted text.

### Technical documentation

In general, this repository provides the transcription module containing several files (see below) which are used to set up a server and transcript audio streams.
It is being used by the *main.py* script, which implements the provided classes

###### Server
```./transcription/server.py```:
* This file contains the **Server** class (Constructor: Server(host, port, uptime, workers)
  * **host** and **port** refer to the ip adress and port of the machine running the server
  * **uptime** is the duration the server runs
  * **workers** is the size of the threadpool
  * To start the server, use **.start()**
* Also, it contains the **AudioProcessorServicer** class, which is the actual server providing the threadpool and handling the connection to the client

```./proto/audioStream.proto```:
* This is the file used for generating the server and client code for the backend and app. It can be regenerated through the ```./regen_proto.sh``` file. The generated files are to be found in ```./generated/*``` and are used by the AudioProcessorServicer

##### Transcription (transcription-gcloud)
```./transcription/processor.py```:
* This file contains the **Processor** class (Constructor: Processor({lang=de_DE, send_interim_results=False}))
  * **lang** is the target language to be expected by the speaker
  * **send_interim_results** toggles whether or not in-between results are submitted by the processor, or only a final transcripted part (which then won't be changed anymore). For our project, we don't want need interim results.
  * One processor is created per incoming request from the server; to start it, invoke .process(stream)

##### Testing
```./transcription/microphone.py```:
* This file provides the Microphone class parallel to the server and is used for testing only (to not having to connect to the phone to test the algorithm)
  * Constructor: Microphone()

##### Main

```./main.py```:
* This is a script implementing the above classes to start and/or test them.
  * Syntax: main.py [input] {arguments}
    * **input** is either "microphone" or "server", depending on whether it's used for testing or deployment
    * **arguments** is a list of arguments passed down to initialize the processor-object

### Future Plans

In the parallel branch transcript-speech2text I started writing my own transcription algorithm, using the [Mozilla Voice Dataset](https://voice.mozilla.org/en).
But since I haven't come very far yet, I won't provide any documentation about that.