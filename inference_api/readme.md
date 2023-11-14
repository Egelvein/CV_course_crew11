### Example of a request

**`POST /file/`**

The method accepts an image file:

```json
{
	"file": "chip.jpg",
}

```

And returns the results of the model detection:

```json
{
	"results": [
        {
            "contour": [
                218.35411071777344,
                0.08491215109825134,
                263.51812744140625,
                27.211015701293945
            ],
            "probability": 0.9038012623786926,
            "class": "missing_hole"
        },
        {
            "contour": [
                190.349609375,
                267.39935302734375,
                223.65646362304688,
                305.36553955078125
            ],
            "probability": 0.8265805244445801,
            "class": "missing_hole"
        }
    ]
}

```
