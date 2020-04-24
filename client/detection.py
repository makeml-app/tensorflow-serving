import PIL.Image
import numpy
import requests
import sys

image = PIL.Image.open(sys.argv[1])
image_np = numpy.array(image)

payload = {"instances": [image_np.tolist()]}
start = time.perf_counter()
res = requests.post("http://<Public IP>:80/v1/models/default:predict", json=payload) #change to your public IP
print(f"Took {time.perf_counter()-start:.2f}s")
pprint(res.json())
