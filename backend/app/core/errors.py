from fastapi import Request, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
import logging

logger = logging.getLogger("banking_chatbot")

class BankingBaseException(Exception):
    """Base exception for all domain-specific banking chatbot errors."""
    def __init__(self, message: str, status_code: int = status.HTTP_400_BAD_REQUEST):
        super().__init__(message)
        self.message = message
        self.status_code = status_code

class InsufficientFundsException(BankingBaseException):
    def __init__(self, message: str = "Insufficient funds to perform this transaction."):
        super().__init__(message, status_code=status.HTTP_400_BAD_REQUEST)

class AccountNotFoundException(BankingBaseException):
    def __init__(self, message: str = "The specified bank account was not found."):
        super().__init__(message, status_code=status.HTTP_404_NOT_FOUND)

class UnauthorizedAgentActionException(BankingBaseException):
    def __init__(self, message: str = "Unauthorized agent operation on sensitive account data."):
        super().__init__(message, status_code=status.HTTP_403_FORBIDDEN)

async def banking_exception_handler(request: Request, exc: BankingBaseException) -> JSONResponse:
    logger.warning(f"Domain validation error at {request.url.path}: {exc.message}")
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "status": "error",
            "message": exc.message,
            "error_type": exc.__class__.__name__
        }
    )

async def http_exception_handler(request: Request, exc: StarletteHTTPException) -> JSONResponse:
    logger.error(f"HTTP exception occurred at {request.url.path}: {exc.detail}")
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "status": "error",
            "message": exc.detail,
            "error_type": "HTTPException"
        }
    )

async def validation_exception_handler(request: Request, exc: RequestValidationError) -> JSONResponse:
    logger.error(f"Validation error occurred at {request.url.path}: {exc.errors()}")
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            "status": "error",
            "message": "Invalid request payload format.",
            "details": exc.errors(),
            "error_type": "RequestValidationError"
        }
    )
