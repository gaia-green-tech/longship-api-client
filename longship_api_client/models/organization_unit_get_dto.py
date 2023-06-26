from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.organization_unit_financial_details_dto import OrganizationUnitFinancialDetailsDto


T = TypeVar("T", bound="OrganizationUnitGetDto")


@attr.s(auto_attribs=True)
class OrganizationUnitGetDto:
    """
    Attributes:
        id (str):
        code (str):
        parent_id (Union[Unset, str]):
        name (Union[Unset, str]): The name of the ou.
        external_reference (Union[Unset, str]): A properties which can be used to link this OU to another system.
        address (Union[Unset, str]):
        state (Union[Unset, str]):
        country (Union[Unset, str]):
        city (Union[Unset, str]):
        house_number (Union[Unset, str]):
        postal_code (Union[Unset, str]):
        hotline_phone_number (Union[Unset, str]):
        company_email (Union[Unset, str]):
        primary_contactperson (Union[Unset, str]):
        primary_contactperson_email (Union[Unset, str]):
        direct_payment_profile_id (Union[Unset, str]):
        msp_ou_id (Union[Unset, str]): The ou id used for the "Msp Integration" feature.
        msp_ou_name (Union[Unset, str]): The ou name used for the "Msp Integration" feature.
        msp_ou_code (Union[Unset, str]): The ou code used for the "Msp Integration" feature.
        msp_external_id (Union[Unset, str]): The externalId from the "Msp Integration" feature.
        financial_details (Union[Unset, OrganizationUnitFinancialDetailsDto]):
    """

    id: str
    code: str
    parent_id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    external_reference: Union[Unset, str] = UNSET
    address: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    country: Union[Unset, str] = UNSET
    city: Union[Unset, str] = UNSET
    house_number: Union[Unset, str] = UNSET
    postal_code: Union[Unset, str] = UNSET
    hotline_phone_number: Union[Unset, str] = UNSET
    company_email: Union[Unset, str] = UNSET
    primary_contactperson: Union[Unset, str] = UNSET
    primary_contactperson_email: Union[Unset, str] = UNSET
    direct_payment_profile_id: Union[Unset, str] = UNSET
    msp_ou_id: Union[Unset, str] = UNSET
    msp_ou_name: Union[Unset, str] = UNSET
    msp_ou_code: Union[Unset, str] = UNSET
    msp_external_id: Union[Unset, str] = UNSET
    financial_details: Union[Unset, "OrganizationUnitFinancialDetailsDto"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        code = self.code
        parent_id = self.parent_id
        name = self.name
        external_reference = self.external_reference
        address = self.address
        state = self.state
        country = self.country
        city = self.city
        house_number = self.house_number
        postal_code = self.postal_code
        hotline_phone_number = self.hotline_phone_number
        company_email = self.company_email
        primary_contactperson = self.primary_contactperson
        primary_contactperson_email = self.primary_contactperson_email
        direct_payment_profile_id = self.direct_payment_profile_id
        msp_ou_id = self.msp_ou_id
        msp_ou_name = self.msp_ou_name
        msp_ou_code = self.msp_ou_code
        msp_external_id = self.msp_external_id
        financial_details: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.financial_details, Unset):
            financial_details = self.financial_details.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "code": code,
            }
        )
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id
        if name is not UNSET:
            field_dict["name"] = name
        if external_reference is not UNSET:
            field_dict["externalReference"] = external_reference
        if address is not UNSET:
            field_dict["address"] = address
        if state is not UNSET:
            field_dict["state"] = state
        if country is not UNSET:
            field_dict["country"] = country
        if city is not UNSET:
            field_dict["city"] = city
        if house_number is not UNSET:
            field_dict["houseNumber"] = house_number
        if postal_code is not UNSET:
            field_dict["postalCode"] = postal_code
        if hotline_phone_number is not UNSET:
            field_dict["hotlinePhoneNumber"] = hotline_phone_number
        if company_email is not UNSET:
            field_dict["companyEmail"] = company_email
        if primary_contactperson is not UNSET:
            field_dict["primaryContactperson"] = primary_contactperson
        if primary_contactperson_email is not UNSET:
            field_dict["primaryContactpersonEmail"] = primary_contactperson_email
        if direct_payment_profile_id is not UNSET:
            field_dict["directPaymentProfileId"] = direct_payment_profile_id
        if msp_ou_id is not UNSET:
            field_dict["mspOuId"] = msp_ou_id
        if msp_ou_name is not UNSET:
            field_dict["mspOuName"] = msp_ou_name
        if msp_ou_code is not UNSET:
            field_dict["mspOuCode"] = msp_ou_code
        if msp_external_id is not UNSET:
            field_dict["mspExternalId"] = msp_external_id
        if financial_details is not UNSET:
            field_dict["financialDetails"] = financial_details

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.organization_unit_financial_details_dto import OrganizationUnitFinancialDetailsDto

        d = src_dict.copy()
        id = d.pop("id")

        code = d.pop("code")

        parent_id = d.pop("parentId", UNSET)

        name = d.pop("name", UNSET)

        external_reference = d.pop("externalReference", UNSET)

        address = d.pop("address", UNSET)

        state = d.pop("state", UNSET)

        country = d.pop("country", UNSET)

        city = d.pop("city", UNSET)

        house_number = d.pop("houseNumber", UNSET)

        postal_code = d.pop("postalCode", UNSET)

        hotline_phone_number = d.pop("hotlinePhoneNumber", UNSET)

        company_email = d.pop("companyEmail", UNSET)

        primary_contactperson = d.pop("primaryContactperson", UNSET)

        primary_contactperson_email = d.pop("primaryContactpersonEmail", UNSET)

        direct_payment_profile_id = d.pop("directPaymentProfileId", UNSET)

        msp_ou_id = d.pop("mspOuId", UNSET)

        msp_ou_name = d.pop("mspOuName", UNSET)

        msp_ou_code = d.pop("mspOuCode", UNSET)

        msp_external_id = d.pop("mspExternalId", UNSET)

        _financial_details = d.pop("financialDetails", UNSET)
        financial_details: Union[Unset, OrganizationUnitFinancialDetailsDto]
        if isinstance(_financial_details, Unset):
            financial_details = UNSET
        else:
            financial_details = OrganizationUnitFinancialDetailsDto.from_dict(_financial_details)

        organization_unit_get_dto = cls(
            id=id,
            code=code,
            parent_id=parent_id,
            name=name,
            external_reference=external_reference,
            address=address,
            state=state,
            country=country,
            city=city,
            house_number=house_number,
            postal_code=postal_code,
            hotline_phone_number=hotline_phone_number,
            company_email=company_email,
            primary_contactperson=primary_contactperson,
            primary_contactperson_email=primary_contactperson_email,
            direct_payment_profile_id=direct_payment_profile_id,
            msp_ou_id=msp_ou_id,
            msp_ou_name=msp_ou_name,
            msp_ou_code=msp_ou_code,
            msp_external_id=msp_external_id,
            financial_details=financial_details,
        )

        organization_unit_get_dto.additional_properties = d
        return organization_unit_get_dto

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