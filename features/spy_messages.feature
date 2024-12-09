Feature: encode or decode a secret message
As a secret spy
I should be able to encode and decode messages
So that I can chat with my spy friends like a pro.

Scenario: I can successfully encode a secret message
    Given I open the url "https://www.hanginghyena.com/solvers_a/caesar-cipher-decoder"
    When I enter "HELLO" in the input field "input"
    And I enter "1" in the input field "shift"
    And I click the element "button[onclick*='encode']"
    And I wait for "200" ms
    Then I expect the element ".output" to have text "IFMMP"

Scenario: I can successfully decode a secret message
    Given I open the url "https://www.hanginghyena.com/solvers_a/caesar-cipher-decoder"
    When I enter "IFMMP" in the input field "input"
    And I enter "1" in the input field "shift"
    And I click the element "button[onclick*='decode']"
    And I wait for "200" ms
    Then I expect the element ".output" to have text "HELLO"