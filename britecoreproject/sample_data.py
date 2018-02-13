"""Sample data for the database."""
from britecoreproject.orm import *
from britecoreproject import dbfunctions

def insert_sample_data():
    """Insert some sample data in the database."""
    # Zeroth, get our database.
    db = dbfunctions.get_db()
    # First, our field type enum.
    ftText = FieldType(fieldTypeName = 'Text')
    ftNumber = FieldType(fieldTypeName = 'Number')
    ftDate = FieldType(fieldTypeName = 'Date')
    ftEnum = FieldType(fieldTypeName = 'Enum')
    # Owner is a human and has some fields pertaining to humans.
    ownerName = Field(fieldName="Owner Name", fieldType=ftText)
    ownerDOB = Field(fieldName="Owner DOB", fieldType=ftDate)
    ownerGender = Field(fieldName="Owner Gender", fieldType=ftText)
    # Driver is a human and has some fields pertaining to humans.
    driverName = Field(fieldName="Driver Name", fieldType=ftText)
    driverDOB = Field(fieldName="Driver DOB", fieldType=ftDate)
    driverGender = Field(fieldName="Driver Gender", fieldType=ftText)
    # Some fields pertaining to automobiles.
    autoMake = Field(fieldName="Automobile Make", fieldType=ftEnum)
    autoModel = Field(fieldName="Automobile Model", fieldType=ftText)
    autoYear = Field(fieldName="Automobile Year", fieldType=ftDate)
    autoMsrp = Field(fieldName="Automobile MSRP (New)", fieldType=ftNumber)
    autoColour = Field(fieldName="Automobile Colour", fieldType=ftEnum)
    autoVin = Field(fieldName="Automobile VIN", fieldType=ftText)
    autoRentalCov = Field(fieldName="Automobile Rental Coverage", fieldType=ftEnum)
    # Some fields pertaining to houses.
    houseAddress = Field(fieldName="House Address", fieldType=ftText)
    houseCity = Field(fieldName="House City", fieldType=ftText)
    houseState = Field(fieldName="House State", fieldType = ftEnum)
    houseZip = Field(fieldName="House ZIP", fieldType=ftText)
    houseCovLimDwel = Field(fieldName="House Coverage Limit - Dwelling", fieldType=ftNumber)
    houseCovLimCont = Field(fieldName="House Coverage Limit - Contents", fieldType=ftNumber)
    houseCovLimOutbuild = Field(fieldName="House Coverage Limit - Outbuildings", fieldType=ftNumber)
    houseCovLimAddExp = Field(fieldName="House Coverage Limit - Additional Expenses", fieldType=ftNumber)
    # Some fields pertaining to prizes.
    prizeAmount = Field(fieldName="Prize Amount", fieldType=ftNumber)
    prizeOdds = Field(fieldName="Prize Odds", fieldType=ftNumber)
    # Some fields pertaining to businesses.
    businessName = Field(fieldName="Business Name", fieldType=ftText)
    businessEstab = Field(fieldName="Business Established", fieldType=ftDate)
    businessAnnualIncome = Field(fieldName="Business Annual Income", fieldType=ftNumber)
    # House is a risk.
    house = RiskType(riskTypeName="House")
    # House has an owner.
    house.addField(ownerName)
    house.addField(ownerDOB)
    house.addField(ownerGender)
    # House has housey fields.
    house.addField(houseAddress)
    house.addField(houseCity)
    house.addField(houseState)
    house.addField(houseZip)
    house.addField(houseCovLimDwel)
    house.addField(houseCovLimCont)
    house.addField(houseCovLimOutbuild)
    house.addField(houseCovLimAddExp)
    # Personal automobile is a risk.
    personalAuto = RiskType(riskTypeName="Personal Automobile")
    # Personal automobile has an owner.
    personalAuto.addField(ownerName)
    personalAuto.addField(ownerDOB)
    personalAuto.addField(ownerGender)
    # Personal automobile has a driver.
    personalAuto.addField(driverName)
    personalAuto.addField(driverDOB)
    personalAuto.addField(driverGender)
    # Personal automobile has automobile-y fields.
    personalAuto.addField(autoMake)
    personalAuto.addField(autoModel)
    personalAuto.addField(autoYear)
    personalAuto.addField(autoMsrp)
    personalAuto.addField(autoColour)
    personalAuto.addField(autoVin)
    personalAuto.addField(autoRentalCov)
    # Business automobile is a risk.
    businessAuto = RiskType(riskTypeName="Business Automobile")
    # Business automobile's owner is a business.
    businessAuto.addField(businessName)
    businessAuto.addField(businessEstab)
    businessAuto.addField(businessAnnualIncome)
    # Business automobile has a driver.
    businessAuto.addField(driverName)
    businessAuto.addField(driverDOB)
    businessAuto.addField(driverGender)
    # Business automobile has automobile-y fields.
    businessAuto.addField(autoMake)
    businessAuto.addField(autoModel)
    businessAuto.addField(autoYear)
    businessAuto.addField(autoMsrp)
    businessAuto.addField(autoColour)
    businessAuto.addField(autoVin)
    businessAuto.addField(autoRentalCov)
    # Prize is a risk.
    prize = RiskType(riskTypeName="Prize")
    # Prize is run by a business.
    prize.addField(businessName)
    prize.addField(businessEstab)
    prize.addField(businessAnnualIncome)
    # Prize has prizey fields.
    prize.addField(prizeAmount)
    prize.addField(prizeOdds)
