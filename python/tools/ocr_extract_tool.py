from agent import Agent
from python.helpers.tool import Tool, Response
from python.helpers import files
from python.helpers.print_style import PrintStyle
import google.generativeai as genai

class Delegation(Tool):
    def execute(self, message="", image_path="", **kwargs):
        response = self.agent.send_vision_message(system="You are an expert in OCR and reading invoices", msg=message, image_path=image_path, output_label="Vision OCR tool")
        return Response(message=response, break_loop=False)

    # def execute_gemini(self, message="", image_path="", **kwargs):
        