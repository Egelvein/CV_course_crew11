from django.forms import Form, FileField


class ImageForm(Form):
    file = FileField(label="Microchip image", max_length=200)
