from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="LocalTokenGroupTokenPostDto")


@attr.s(auto_attribs=True)
class LocalTokenGroupTokenPostDto:
    """
    Attributes:
        is_valid (Union[Unset, bool]):
        name (Union[Unset, str]):
        uid (Union[Unset, str]):
        contract_id (Union[Unset, str]):
    """

    is_valid: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    uid: Union[Unset, str] = UNSET
    contract_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        is_valid = self.is_valid
        name = self.name
        uid = self.uid
        contract_id = self.contract_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_valid is not UNSET:
            field_dict["isValid"] = is_valid
        if name is not UNSET:
            field_dict["name"] = name
        if uid is not UNSET:
            field_dict["uid"] = uid
        if contract_id is not UNSET:
            field_dict["contractId"] = contract_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        is_valid = d.pop("isValid", UNSET)

        name = d.pop("name", UNSET)

        uid = d.pop("uid", UNSET)

        contract_id = d.pop("contractId", UNSET)

        local_token_group_token_post_dto = cls(
            is_valid=is_valid,
            name=name,
            uid=uid,
            contract_id=contract_id,
        )

        local_token_group_token_post_dto.additional_properties = d
        return local_token_group_token_post_dto

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties