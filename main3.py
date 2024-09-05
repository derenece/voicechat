
import torch
import transformers
from parler_tts import ParlerTTSForConditionalGeneration
import soundfile as sf


def text_to_speech(generated_text, outpath):

    torch.cuda.empty_cache()

    device = "cpu" 

    model = ParlerTTSForConditionalGeneration.from_pretrained("parler-tts/parler_tts_mini_v0.1").to(device)
    tokenizer = transformers.AutoTokenizer.from_pretrained("parler-tts/parler_tts_mini_v0.1", use_fast=True)

    #prompt = "Include the term 'very clear audio' to generate the highest quality audio, and 'very noisy audio' for high levels of background noise!"
    description = "A female speaker with a slightly low-pitched voice delivers her words quite expressively, in a very confined sounding environment with clear audio quality. She speaks very fast."

    input_ids = tokenizer(description, return_tensors="pt").input_ids.to(device)
    prompt_input_ids = tokenizer(generated_text, return_tensors="pt").input_ids.to(device)

    generation = model.generate(input_ids=input_ids, prompt_input_ids=prompt_input_ids)
    audio_url = generation.cpu().numpy().squeeze()
    #sf.write("parler_tts_out.wav", audio_arr, model.config.sampling_rate)

    sf.write(outpath, audio_url, model.config.sampling_rate)

    return generated_text


