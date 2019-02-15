import re
import unicodedata

class IgboText():
    """The IgboText Class preprocesses texts written in Igbo language for further nlp tasks
    """
    def normalize(self, text, convert_to_lower=True, remove_abbreviations=True):
        """Normalizes a text written in Igbo Language.
        # Example Usage
            igbotext = IgboText()
            igbotext.normalize("N’ụlọ Akwụkwọ") -> n ụlọ akwụkwọ
            igbotext.normalize("N’ụlọ Akwụkwọ", False) -> N ụlọ Akwụkwọ

        # Arguments
            text: String to normalize
            convert_to_lower: Boolean toggle to either keep the upper case 
            letters or convert them to lower case
            remove_abbreviations: Toggle to remove abbreviations in the text.

        # Returns
            text: Normalized string

        # Raises
            TypeError if text is None, empty or not a string
        """
        if text is None:
            raise TypeError("The parameter text is of the type NoneType")

        if not isinstance(text, str):
            raise TypeError("The parameter text has to be a string")

        if text == "":
            raise TypeError("The parameter text is empty")

        if convert_to_lower:
            text = text.lower()
        text = self.__remove_tonal_marks__(text)
        text = self.__remove_digits_and_special_characters__(text,
                                                         remove_abbreviations)
        text = self.__split_combined_words__(text, False)
        return text.strip()

    def tokenize(self, text, convert_to_lower=False):
        """Tokenizes a text written in Igbo Language into a list of Igbo words.
        # Example Usage
            igbotext = IgboText()
            igbotext.tokenize("N’ụlọ Akwụkwọ") -> ['N’', 'ụlọ', 'Akwụkwọ']
            igbotext.normalize("N’ụlọ Akwụkwọ", True) 
            -> ['n’', 'ụlọ', 'akwụkwọ']

        # Arguments
            text: String to tokenize
            convert_to_lower: Boolean toggle to either keep the upper case 
            letters or convert them to lower case

        # Returns
            token_list: List containing tokens

        # Raises
            TypeError if text is None, empty or not a string
        """
        if text is None:
            raise TypeError("The parameter text is of the type NoneType")
            
        if not isinstance(text, str):
            raise TypeError("The parameter text has to be a string")

        if text == "":
            raise TypeError("The parameter text is empty")

        if convert_to_lower:
            text = text.lower()
        text = self.__remove_tonal_marks__(text)
        text = self.__space_out_symbols__(text)
        text = self.__split_combined_words__(text)
        token_list = text.strip().split()
        return token_list


    def __remove_tonal_marks__(self, text):
        """Removes tonal marks in the provided text.
        # Arguments
            text: String to remove tonal marks
        
        # Returns
            text: String with tonal marks removed.
        """
        text_characters = []
        for c in text:
            #Remove markings
            if unicodedata.category(c) == "Mn":
                continue
            elif ord(c) > 128 and ord(c) < 300:
                c = unicodedata.normalize('NFD', c)
                c = c.encode('ascii', 'ignore').decode('utf-8')
                text_characters.append(c)
            else:
                text_characters.append(c)
        return "".join(text_characters)

    def __remove_digits_and_special_characters__(self, text, remove_abbreviations=True):
        """Removes digits, symbols and non igbo words in the provided text.
        # Arguments
            text: String containing digits and non igbo words.
            remove_abbreviations: Toggle to remove abbreviations in the text.
        
        # Returns
            text: String with digits, symbols and non igbo words
        """
        #remove abbreviations if remove_abbreviations is true
        if remove_abbreviations:
            text = re.sub(r"(?:[a-zA-Z]\.){2,}", "", text)
        text = re.sub(r"([?.!,¿])", r" \1 ", text)
        regexp = re.compile(r"[a-zA-ZỊịṄṅỌọỤụ\-\'\’]+")
        splited_text = text.split()
        good_texts = []
        for word in splited_text:
            match = regexp.search(word)
            if match is not None and match.span()[1] == len(word):
                good_texts.append(word)
        return " ".join(good_texts)

    def __split_combined_words__(self, text, keep_symbols=True):
        """Split words combined with the hyphen and aprostrophe into two words
        # Arguments:
            text: String containing combined words.
            keep_symbols: Boolean toggle to still keep symbol or not.

        # Returns:
            text: String containing un-combined words.
        """
        if keep_symbols:
            text = re.sub(r"([-’'])", r"\1 ", text)
        else:
            text = re.sub(r"([-’'])", r" ", text)
        return text

    def __space_out_symbols__(self, text):
        """Adds space before and after some punctuation marks 
        # Arguments:
            text: String containing punctuation marks.

        # Returns:
            text: Processed string.
        """
        text = re.sub(r"([?.!:;,¿<>(){}[\]])", r" \1 ", text)
        #Remove quote found at the beginning of a word
        text = re.sub(r"\s+([-'\"‘’“”])", r" \1 ", text)
        text = re.sub(r"([-'\"‘’“”])\s+", r" \1 ", text)
        text = re.sub(r"([-'\"‘’“”])$", r" \1", text)
        text = re.sub(r"^([-'\"‘’“”])", r"\1 ", text)
        return text