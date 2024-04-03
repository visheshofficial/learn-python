import pytest
from survey import AnonymousSurvey

@pytest.fixture
def language_survey():
    """Create a survey instance for use in all test methods."""
    question = "What language did you first learn to speak?"
    return AnonymousSurvey(question)

def test_store_singal_resposne_with_fixture(language_survey):
        """Test that a single response is stored properly."""
        language_survey.store_response('Marathi')
        assert 'Marathi' in language_survey.responses

def test_store_three_responses_with_fixture(language_survey):
    """Test that three individual responses are stored properly."""
    responses = ['English', 'Spanish', 'Mandarin']
    for response in responses:
        language_survey.store_response(response)

    for response in responses:
        assert response in language_survey.responses

def test_store_single_response():
    """Test that a single response is stored properly."""
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)
    language_survey.store_response('English')
    assert 'English' in language_survey.responses
    
def test_store_three_responses():
    """Test that three individual responses are stored properly."""
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)
    responses = ['English', 'Spanish', 'Mandarin']
    for response in responses:
        language_survey.store_response(response)

    for response in responses:
        assert response in language_survey.responses