
# import torch
# import transformers

from maip_client import MaipClient
from maip_context import MaipContext

def text_to_text(transcripted_text):

    myClient = MaipClient("192.168.68.131", 8070)
    myClient.create_client()

    hostedModel = myClient.get_program_models()[0]

    myClient.acquire_model(hostedModel)
    chatObject : MaipContext = myClient.create_context(hostedModel, 4096)

    # print(myClient.get_program_models())
    # device="cpu"

    # # Load pre-trained Qwen2 tokenizer and model
    # tokenizer = transformers.AutoTokenizer.from_pretrained("Qwen/Qwen2-1.5B-Instruct")


    # model = transformers.AutoModelForCausalLM.from_pretrained("Qwen/Qwen2-1.5B-Instruct") # larger models are slower but better than smaller ones
    # model.to(device)
    # print(f"Using device: {device}")


    # examples = (
    #     "user: What is the capital of France?\n"
    #     "assistant: The capital of France is Paris.\n\n"
    #     "user: Write the first three big cities of Turkey.\n"
    #     "assistant: The first three big cities of Turkey are Istanbul, Ankara, and Izmir.\n\n"
    #     "user: However far away, I will always love you. However long I stay, I will always love you.\n"
    #     "assistant: Whatever words I say, I will always love you. I will always love you.\n\n"
    # )

    input = transcripted_text

    msgIds = []

    messageId = chatObject.set_input("System", "You are an AI assistant designed to transcribe instructions, generate responses to questions, and summarize text." + "You are a helpful assistant and you want to answer people's questions. If you know the exact answer, please answer; otherwise, say that 'I don't know.'\n\n")
    msgIds.append(messageId)
    messageId = chatObject.set_input("User", input)
    msgIds.append(messageId)

    myResult = chatObject.execute_input_sync(msgIds)
    
    # prompt = (
    #     #f"assistant: Below you can find the example conversation between user and assistant. "
    #     f"You are an AI assistant designed to transcribe instructions, generate responses to questions, and summarize text."
    #     f"You are a helpful assistant and you want to answer people's questions. If you know the exact answer, please answer; otherwise, say that 'I don't know.'\n\n"
    #     #f"{examples}"
    #     f"user: {input}\n"
    #     f"assistant:"
    # )

    # inputs = tokenizer.encode(prompt, return_tensors="pt").to(device)  # Ensure input_ids are on the same device as the model


    # attention_mask = torch.ones(inputs.shape, dtype=torch.long).to(device)

    # outputs = model.generate(inputs, 
    #                 attention_mask=attention_mask,
    #                 max_length=300, 
    #                 pad_token_id=tokenizer.eos_token_id,
    #                 eos_token_id=tokenizer.eos_token_id,
    #                 repetition_penalty=1.2,
    #                 temperature=0.7,
    #                 do_sample=True,
    #                 top_p=0.9,
    #                 num_return_sequences=1)


    # text = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # answer = text.split("assistant:", 1)[1] #divide the string at the first occurence of the substring "assistant:"
    # print("Answer:\n", answer)

    # return answer
    return myResult