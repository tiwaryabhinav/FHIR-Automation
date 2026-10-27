from fastapi import APIRouter, UploadFile, File, Form
from pydantic import BaseModel
from service.doc_verify import DocVerify

router = APIRouter(prefix="/doc")
doc_verify_service = DocVerify()


class ApprovalRequest(BaseModel):
    decision: str
    summary: str | None = None

@router.get("/test")
def testAPI():
        return {
            "message" : "API is running"
        }

@router.post("/checkDoc")
async def checkDoc(patientId: str = Form(...), reviewId: str = Form(...), file: UploadFile = File(...)):
        #Uploaded file can be like a pdf or a image or a text file.
        #We need to check if that file contains valid field for CarePlan team to proceed.
        #If yes, well just return all okay like message in response.
        #If no, check which fields are missing.
        #Return a summary message generated with the help of LLM to previous team.
    print("doc controller reached for patientId: ", patientId)
    return await doc_verify_service.verify_doc(patientId, reviewId, file)

@router.post("/approve")
async def humanReview(reviewId: str, payload: ApprovalRequest):
    """This controller is responsible for human review decision of generated summary by LLM"""

    print("reviewId - ", reviewId, " - decision - ", payload.decision)
    return await doc_verify_service.approve_summary(
        reviewId,
        payload.decision,
        payload.summary,
    )
