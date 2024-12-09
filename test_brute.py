import pytest
from brute import Brute

def describe_Brute():
    @pytest.fixture
    def cracker():
        return Brute("secret")
    
    def describe_bruteOnce():
        def it_returns_true_when_correct_password(cracker):
            assert cracker.bruteOnce("secret") == True
        
        def it_returns_false_when_wrong_password(cracker):
            assert cracker.bruteOnce("wrong") == False
            
    def describe_bruteMany():
        def it_succeeds_when_guess_matches(cracker, mocker):
            mocker.patch.object(cracker, 'randomGuess', return_value="secret")
            mocker.patch('time.time', return_value=0)
            
            result = cracker.bruteMany(limit=1)
            assert result >= 0 
            
        def it_fails_after_all_attempts(cracker, mocker):
            mocker.patch.object(cracker, 'randomGuess', return_value="wrong")
            mocker.patch('time.time', return_value=0)
            
            result = cracker.bruteMany(limit=3)
            assert result == -1 