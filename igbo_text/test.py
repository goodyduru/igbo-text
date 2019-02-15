import unittest
from .module import IgboText
class TestIgboText(unittest.TestCase):

    def test_remove_tonal_mark(self):
        igbo_text = IgboText()
        self.assertEqual(igbo_text.__remove_tonal_marks__("Ọ nà-ezò nnukwu mmīri n'iro"), "Ọ na-ezo nnukwu mmiri n'iro")

    def test_remove_digits_and_special_characters(self):
        igbo_text = IgboText()

        self.assertEqual(igbo_text.__remove_digits_and_special_characters__("Nnukwu mmiri na-ezo n'iro C.E.O."), "Nnukwu mmiri na-ezo n'iro")

        #Test remove_abbreviations = False
        self.assertEqual(igbo_text.__remove_digits_and_special_characters__("Nnukwu mmiri na-ezo n'iro C.E.O.", False), "Nnukwu mmiri na-ezo n'iro C E O")

    def test_split_combined_words(self):
        igbo_text = IgboText()
        self.assertEqual(igbo_text.__split_combined_words__("Ndị Fàda kwènyèrè n'atọ̀ n'ime otù."), "Ndị Fàda kwènyèrè n' atọ̀ n' ime otù.")

        #Test keep_symbol = False
        self.assertEqual(igbo_text.__split_combined_words__("Ndị Fàda kwènyèrè n'atọ̀ n'ime otù.", False), "Ndị Fàda kwènyèrè n atọ̀ n ime otù.")

    def test_space_out_symbols(self):
        igbo_text = IgboText()
        self.assertEqual(igbo_text.__space_out_symbols__("'Ọ nà-ezò nnukwu mmīri n'iro?'"), "' Ọ nà-ezò nnukwu mmīri n'iro ?  ' ")

    def test_normalize(self):
        igbo_text = IgboText()

        with self.assertRaises(TypeError):
            igbo_text.normalize("")
        
        with self.assertRaises(TypeError):
            igbo_text.normalize(None)

        self.assertEqual(igbo_text.normalize("'Ọ nà-ezò nnukwu mmīri n'iro?'"), "ọ na ezo nnukwu mmiri n iro")

        #Test convert_to_lower = False
        self.assertEqual(igbo_text.normalize("'Ọ nà-ezò nnukwu mmīri n'iro?'", False), "Ọ na ezo nnukwu mmiri n iro")

        #Test remove abbreviation = True
        self.assertEqual(igbo_text.normalize("'Ọ nà-ezò nnukwu mmīri n'iro U.S.A.?'"), "ọ na ezo nnukwu mmiri n iro")

        #Test remove abbreviation = False
        self.assertEqual(igbo_text.normalize("'Ọ nà-ezò nnukwu mmīri n'iro U.S.A.?'", remove_abbreviations=False), "ọ na ezo nnukwu mmiri n iro u s a")

        #Test convert_to_lower = False, remove abbreviation = False
        self.assertEqual(igbo_text.normalize("'Ọ nà-ezò nnukwu mmīri n'iro U.S.A.?'", convert_to_lower=False, remove_abbreviations=False), "Ọ na ezo nnukwu mmiri n iro U S A")

    def test_tokenize(self):
        igbo_text = IgboText()

        with self.assertRaises(TypeError):
            igbo_text.normalize("")
        
        with self.assertRaises(TypeError):
            igbo_text.normalize(None)

        self.assertListEqual(igbo_text.tokenize("Ndị Fàda kwènyèrè n'atọ̀ n'ime otù."), ["Ndị", "Fada", "kwenyere", "n'", "atọ", "n'", "ime", "otu", "."])

        #Test convert_to_lower = False
        self.assertListEqual(igbo_text.tokenize("Ndị Fàda kwènyèrè n'atọ̀ n'ime otù.", convert_to_lower=True), ["ndị", "fada", "kwenyere", "n'", "atọ", "n'", "ime", "otu", "."])

if __name__ == "__main__":
    unittest.main()