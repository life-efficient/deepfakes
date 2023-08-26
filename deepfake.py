# %%
import onnx
import os

os.chdir("/Users/ice/lectures/workbench/projects/youtube/deepfakes")

# https://drive.google.com/file/d/1krOLgjW2tAPaqV-Bw4YALz0xT5zlb5HF/view
model = onnx.load("inswapper_128.onnx")
# %%
onnx.checker.check_model(model)

# Print a human readable representation of the graph
print(onnx.helper.printable_graph(model.graph))
# %%
