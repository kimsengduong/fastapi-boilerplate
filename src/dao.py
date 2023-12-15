from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.orm import Session

import colorama
from src.db import SessionLocal

ModelType = TypeVar("ModelType", bound=Any)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)

Session = SessionLocal


class BaseDAO(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    model = None

    # def __init__(self, model: Type[ModelType]):
    #     """
    #     CRUD object with default methods to Create, Read, Update, Delete (CRUD).

    #     **Parameters**

    #     * `model`: A SQLAlchemy model class
    #     * `schema`: A Pydantic model (schema) class
    #     """
    #     self.model = model

    def get(self, id: Any) -> Optional[ModelType]:
        return Session.query(self.model).filter(self.model.id == id).first()

    def get_all(self, **kwargs) -> List[ModelType]:
        page = kwargs.get("page", 1)
        limit = kwargs.get("limit", 100)
        offset = (page - 1) * limit
        return Session.query(self.model).offset(offset).limit(limit).all()

    def create(self, *, obj_in: CreateSchemaType) -> ModelType:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)  # type: ignore
        Session.add(db_obj)
        Session.commit()
        Session.refresh(db_obj)
        return db_obj

    # def update(
    #     self, *, db_obj: ModelType, obj_in: Union[UpdateSchemaType, Dict[str, Any]]
    # ) -> ModelType:
    #     obj_data = jsonable_encoder(db_obj)
    #     if isinstance(obj_in, dict):
    #         update_data = obj_in
    #     else:
    #         update_data = obj_in.dict(exclude_unset=True)
    #     for field in obj_data:
    #         if field in update_data:
    #             setattr(db_obj, field, update_data[field])
    #     Session.add(db_obj)
    #     Session.commit()
    #     Session.refresh(db_obj)
    #     return db_obj

    def update(
        self, *, id: int, obj_in: Union[UpdateSchemaType, Dict[str, Any]]
    ) -> ModelType:
        obj = Session.query(self.model).get(id)
        print(colorama.Fore.RED, "obj", obj, colorama.Style.RESET_ALL)
        obj_data = jsonable_encoder(obj)
        print(colorama.Fore.RED, "obj_data", obj_data, colorama.Style.RESET_ALL)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        for field in obj_data:
            if field in update_data:
                setattr(obj, field, update_data[field])
        # Session.add(obj)
        Session.commit()
        Session.refresh(obj)
        return obj

    def remove(self, *, id: int) -> ModelType:
        obj = Session.query(self.model).get(id)
        Session.delete(obj)
        Session.commit()
        return obj
