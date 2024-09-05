document.addEventListener('DOMContentLoaded', 
    function (){
    let record_button = document.getElementById("record_button");

    let stop_button = document.getElementById("stop_button");

    let upload_form = document.getElementById("upload_form");

    let audio_file_input = document.getElementById("audio_file");

    //to handle audio recording
    let media_recorder;
    let audio_chunks = [];

    record_button.addEventListener("click", async () => {
        
        //navigator.mediaDevices.getUserMedia({audio:true}) used to request access to user's media devices (e.g. mic, camera, screen)
        //'{ audio:true}' specifies that only audio (mic) access is required
        //'await' keyword is used to wait for the promise to resolve, pausing the execution of the function until the stream is available.
        let stream = await navigator.mediaDevices.getUserMedia({ audio: true });
       
        // This 'stream' contains the audio data from the user's microphone.
        //create MediaRecorder instance that will be used to record the audio from the MediaStream obtained in the previous step.
        media_recorder = new MediaRecorder(stream);

        //Start recording
        media_recorder.start();
        record_button.disabled = true;
        stop_button.disabled = false;

        //'dataavailable' event is fired whenever the MediaRecorder has media data available to be captured, during the recording process. 
        //The event carries this data in the form of Blob objects.
        media_recorder.addEventListener("dataavailable", event => {
            //The event object contains a data property, which holds the media data in the form of a Blob object.
            // A 'Blob' (Binary Large Object) is a file-like obj. representing raw data
            // array that collects all the chunks of audio data captured during the recording session
            audio_chunks.push(event.data);
        });


        //'stop' event fired when the recording has stopped
        //// Code inside this function executes when the recording stops
        media_recorder.addEventListener("stop", () => {
            //Create 'Blob' obj from collected audio chunks
            // {type:'audio/wav'} Indicates that the data is audio in WAV flaw
            let audio_blob = new Blob(audio_chunks, { type: "audio/wav" });

            //Generate URL to represent Blob obj.
            //This URL can be used as the source of an audio element
            let audio_url = URL.createObjectURL(audio_blob);

            //Generate Audio object using URL
            let audio = new Audio(audio_url);

            //Play the audio
            audio.play();

            //Create File object from Blob
            let file = new File([audio_blob], "recorded_audio.wav", { type: "audio/wav" });
            
            //DataTransfer obj. is created for drag-drop file uploads.
            let data_transfer = new DataTransfer();

            //Adds 'File' obj. to 'DataTransfer' obj.'s items
            data_transfer.items.add(file);

            //Sets 'files' property of file input to 'DataTransfer' object's file.
            audio_file_input.files = data_transfer.files;
            
            upload_form.style.display = "block"; // Make the form visible temporarily
            upload_form.submit(); // Submit the form programmatically
        });
    });

    stop_button.addEventListener("click", () => {
        media_recorder.stop();
        record_button.disabled = false;
        stop_button.disabled = true;
        });
    }
);
