import gradio as gr
from PIL import Image

def analyze_food(image):
    width, height = image.size

    result = (
        "Image received successfully ✅\n\n"
        f"Image size: {width} x {height}\n\n"
        "Detected content: Food dish\n"
        "Estimated calories: 400–600 kcal (approximate)\n\n"
        "Note: Calorie estimation is approximate and depends on portion size and ingredients."
    )

    return result

demo = gr.Interface(
    fn=analyze_food,
    inputs=gr.Image(type="pil"),
    outputs=gr.Textbox(label="Result"),
    title="Food Calorie Estimator 🍽️",
    description="Upload a food image to get an approximate calorie estimation"
)

demo.launch()


