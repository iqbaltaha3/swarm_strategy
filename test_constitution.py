import unittest

from constitution.loader import inject_constitution_into_prompt, merge_constitutions


class ConstitutionLoaderTests(unittest.TestCase):
    def test_merge_includes_global_and_agent_specific_constitutions(self):
        merged = merge_constitutions("plaintiff_strategy")

        self.assertIn("global", merged)
        self.assertIn("agent_specific", merged)
        self.assertEqual(merged["agent_name"], "plaintiff_strategy")
        self.assertEqual(merged["global"]["name"], "Global Legal Strategy Constitution")
        self.assertEqual(merged["agent_specific"]["role"], "Plaintiff Advocate Strategist")

    def test_injected_prompt_contains_both_constitution_sources(self):
        prompt = inject_constitution_into_prompt("System prompt", "plaintiff_strategy")

        self.assertIn("CONSTITUTION FOR PLAINTIFF ADVOCATE STRATEGIST", prompt)
        self.assertIn("Develop strongest possible arguments and strategies from plaintiff perspective", prompt)
        self.assertIn("All analysis must be grounded in factual information provided", prompt)
        self.assertIn("System prompt", prompt)


if __name__ == "__main__":
    unittest.main()
