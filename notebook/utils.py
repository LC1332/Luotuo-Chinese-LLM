import torch


class DeviceMap:
    __top_layer: str
    __device_map: dict
    __total_layers: int
    __layers: int

    def __init__(self, model=None):
        if model == "LLaMA":
            self.__top_layer = "model"
            self.__device_map = {
                "model.embed_tokens": 0,
                "model.norm": 0,
                "lm_head": 0,
            }
            self.__total_layers = 34
            self.__layers = 32

        elif model == "ChatGLM":
            self.__top_layer = "transformer"
            self.__device_map = {
                "transformer.word_embeddings": 0,
                "transformer.final_layernorm": 0,
                "lm_head": 0,
            }
            self.__total_layers = 30
            self.__layers = 28

        else:
            self.__top_layer = ""
            self.__device_map = {"": 0}
            self.__total_layers = 0
            self.__layers = 0

    def get(self):
        top_layer = self.__top_layer
        total_layers = self.__total_layers
        layers = self.__layers
        device_map = self.__device_map

        free_gpu_mem = torch.cuda.mem_get_info()
        min_id = min(enumerate(free_gpu_mem), key=lambda x: x[1])[0]
        max_id = max(enumerate(free_gpu_mem), key=lambda x: x[1])[0]

        totol_mem = sum(free_gpu_mem)

        world_layers = {
            id: int(round(total_layers * (mem / totol_mem))) 
            for id, mem in enumerate(free_gpu_mem)
        }

        diff = total_layers - sum(world_layers.values())
        world_layers[max_id if diff > 0 else min_id] += diff

        cnt = total_layers - layers
        gpu_id = 0

        for i in range(layers):
            if cnt < world_layers[gpu_id]:
                cnt += 1
            else:
                gpu_id += 1
                cnt = 1
            device_map[f"{top_layer}.layers.{i}"] = gpu_id

        return device_map

    def peft(self):
        prefix = "base_model.model"
        device_map = self.get()
        perf_device_map = {"": 0}
        for k, v in device_map.items():
            perf_device_map[f"{prefix}.{k}"] = v
        return perf_device_map
