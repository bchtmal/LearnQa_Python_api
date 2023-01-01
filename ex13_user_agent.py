import json

import pytest
import requests


class TestUserAgent:
    user_agent_list = [
        (
            "Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
            "Mobile", "No", "Android"),
        (
            "Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1",
            "Mobile", "Chrome", "iOS"),
        ("Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
         "Googlebot", "Unknown", "Unknown"),
        (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0",
            "Web", "Chrome", "No"),
        (
            "Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
            "Mobile", "No", "iPhone")
    ]

    user_agent_check_url = "https://playground.learnqa.ru/ajax/api/user_agent_check"

    @pytest.mark.parametrize('user_agent, platform, browser, device', user_agent_list)
    def test_user_agent_check(self, user_agent, platform, browser, device):
        user_agent_check_response = requests.get(self.user_agent_check_url, headers={
            "User-Agent": user_agent})
        user_agent_check_json = json.loads(user_agent_check_response.text)
        assert user_agent_check_json[
                   "platform"] == platform, f"Response parameter 'platform' is not correct: {user_agent_check_json['platform']}. Expected: {platform}"
        assert user_agent_check_json[
                   "browser"] == browser, f"Response parameter 'browser' is not correct: {user_agent_check_json['browser']}. Expected: {browser}"
        assert user_agent_check_json[
                   "device"] == device, f"Response parameter 'device' is not correct: {user_agent_check_json['device']}. Expected: {device}"