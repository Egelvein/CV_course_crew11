var canvas = document.getElementById('canvas');
var context = canvas.getContext('2d');
const video = document.querySelector("#videoElement");

video.width = 400;
video.height = 300;
if (navigator.mediaDevices.getUserMedia) {
    navigator.mediaDevices.getUserMedia({
        video: true
    })
        .then(function (stream) {


            video.srcObject = stream;
            video.play();
        })
        .catch(function (err0r) {

        });
}
var timeLeft = 45;
var timerId = setInterval(countdown, 1000);

function countdown() {
    if (timeLeft == 0) {
        clearTimeout(timerId);

        return '..'
    } else {
        timeLeft--;
        width = video.width;
        height = video.height;
        context.drawImage(video, 0, 0, width, height);
        var dataa = canvas.toDataURL('image/jpeg', 0.5);
        context.clearRect(0, 0, width, height);
        $.ajax({
                type: 'POST',
                url: "{% url 'Start_Webcam'  %}",
                data: {
                    'image': data,
                    csrfmiddlewaretoken: '{{ csrf_token }}'
                },
                success: function (data) {
                    console.log(data)
                },
                error: function (response) {
                    console.log('Error')
                },
            }
        );
    }
}