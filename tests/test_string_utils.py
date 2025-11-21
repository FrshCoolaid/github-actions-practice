"""
Tests for string_utils module.
"""

import pytest
from src.string_utils import (
    reverse_string,
    is_palindrome,
    count_vowels,
    capitalize_words,
    remove_whitespace
)


class TestReverseString:
    """Tests for reverse_string function."""
    
    def test_reverse_simple_string(self):
        """Test reversing simple strings."""
        assert reverse_string("hello") == "olleh"
        assert reverse_string("world") == "dlrow"
    
    def test_reverse_palindrome(self):
        """Test reversing palindromes."""
        assert reverse_string("racecar") == "racecar"
    
    def test_reverse_empty_string(self):
        """Test reversing empty string."""
        assert reverse_string("") == ""
    
    def test_reverse_single_character(self):
        """Test reversing single character."""
        assert reverse_string("a") == "a"
    
    def test_reverse_with_spaces(self):
        """Test reversing strings with spaces."""
        assert reverse_string("hello world") == "dlrow olleh"


class TestIsPalindrome:
    """Tests for is_palindrome function."""
    
    def test_palindrome_simple(self):
        """Test simple palindromes."""
        assert is_palindrome("racecar") == True
        assert is_palindrome("level") == True
        assert is_palindrome("noon") == True
    
    def test_not_palindrome(self):
        """Test non-palindromes."""
        assert is_palindrome("hello") == False
        assert is_palindrome("world") == False
    
    def test_palindrome_with_spaces(self):
        """Test palindromes with spaces."""
        assert is_palindrome("race car") == True
        assert is_palindrome("a man a plan a canal panama") == True
    
    def test_palindrome_mixed_case(self):
        """Test palindromes with mixed case."""
        assert is_palindrome("RaceCar") == True
        assert is_palindrome("LeVeL") == True
    
    def test_single_character(self):
        """Test single character (always palindrome)."""
        assert is_palindrome("a") == True


class TestCountVowels:
    """Tests for count_vowels function."""
    
    def test_count_vowels_simple(self):
        """Test counting vowels in simple strings."""
        assert count_vowels("hello") == 2  # e, o
        assert count_vowels("world") == 1  # o
    
    def test_count_vowels_all_vowels(self):
        """Test string with all vowels."""
        assert count_vowels("aeiou") == 5
        assert count_vowels("AEIOU") == 5
    
    def test_count_vowels_no_vowels(self):
        """Test string with no vowels."""
        assert count_vowels("xyz") == 0
        assert count_vowels("bcdfg") == 0
    
    def test_count_vowels_empty_string(self):
        """Test empty string."""
        assert count_vowels("") == 0
    
    def test_count_vowels_mixed_case(self):
        """Test mixed case vowels."""
        assert count_vowels("HeLLo WoRLd") == 3


class TestCapitalizeWords:
    """Tests for capitalize_words function."""
    
    def test_capitalize_simple(self):
        """Test capitalizing simple strings."""
        assert capitalize_words("hello world") == "Hello World"
    
    def test_capitalize_already_capitalized(self):
        """Test already capitalized strings."""
        assert capitalize_words("Hello World") == "Hello World"
    
    def test_capitalize_all_lowercase(self):
        """Test all lowercase."""
        assert capitalize_words("the quick brown fox") == "The Quick Brown Fox"
    
    def test_capitalize_single_word(self):
        """Test single word."""
        assert capitalize_words("hello") == "Hello"
    
    def test_capitalize_empty_string(self):
        """Test empty string."""
        assert capitalize_words("") == ""


class TestRemoveWhitespace:
    """Tests for remove_whitespace function."""
    
    def test_remove_spaces(self):
        """Test removing spaces."""
        assert remove_whitespace("hello world") == "helloworld"
    
    def test_remove_multiple_spaces(self):
        """Test removing multiple spaces."""
        assert remove_whitespace("hello    world") == "helloworld"
    
    def test_remove_tabs_and_newlines(self):
        """Test removing tabs and newlines."""
        assert remove_whitespace("hello\tworld\n") == "helloworld"
    
    def test_no_whitespace(self):
        """Test string with no whitespace."""
        assert remove_whitespace("helloworld") == "helloworld"
    
    def test_only_whitespace(self):
        """Test string with only whitespace."""
        assert remove_whitespace("   \t\n  ") == ""