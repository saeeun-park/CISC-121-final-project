import gradio as gr
#bubble sort algorithm

def bubble_sort_steps(numbers):
    steps=[]
    arr = numbers[:]
    
    n=len(arr)
    for i in range(n):
        for j in range(n-1-i):
            if arr[j]>arr[j+1]:
                temp=arr[j]
                arr[j], arr[j+1] = arr[j+1], arr[j]
        steps.append(arr[:])
            
    return steps

def run_sort(text):
    try:
        numbers=[int(x.strip()) for x in text.split(",")]
    except:
        return "Error: Please enter numbers separated by commas."

    steps = bubble_sort_steps(numbers)

    result=""
    for i, step in enumerate(steps):
        result += f"step {i+1}:{step}\n"

    return result

with gr.Blocks() as demo:
    gr.Markdown("### Bubble Sort")
    input_box = gr.Textbox(label="Enter numbers")
    output_box= gr.Textbox(label="Sotring Steps", lines=15)
    button=gr.Button("Run Sort")
    button.click(run_sort, input_box, output_box)

demo.launch()
