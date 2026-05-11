from fastapi import APIRouter
from reportlab.pdfgen import canvas
import io

router = APIRouter()


@router.get("/report")
def report():

    buffer = io.BytesIO()
    c = canvas.Canvas(buffer)

    c.setFont("Helvetica", 14)
    c.drawString(100, 800, "Quantum AI Portfolio Report")

    c.setFont("Helvetica", 10)
    c.drawString(100, 770, "Classical + AI + Quantum Optimization System")
    c.drawString(100, 750, "Includes Risk + Backtesting + Forecasting")

    c.drawString(100, 720, "Generated Successfully")

    c.save()

    buffer.seek(0)

    return {"message": "Report generated"}