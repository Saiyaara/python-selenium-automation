# Created by charjapadamin at 26/6/21
Feature: User can open and close window
# Enter feature name here
  # Enter feature description here

  Scenario: User can open and close Amazon Privacy notice
  Given Open Amazon T&C 508088 page
    When Store original windows
    When Click on Amazon Privacy Notice link
    When Switch to the newly opened window
    Then Verify Amazon Privacy Notice Page is opened
    When User can close new window
    When switch back to original