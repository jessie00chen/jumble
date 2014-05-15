#!/usr/bin/env ruby
require 'pry'

class String
	def self.jumble(words, dictionary_path)
		puts
		puts "Input is #{words}"
		input = count_dict(words)

		File.open(dictionary_path, "r") { |f|
			f.each_line { |item|
				copy_input = input.dup
				valid = true
				item.strip!	
				item.each_char { |t|
					break valid = false if copy_input[t].nil?
					copy_input[t] = copy_input[t] - 1
					break valid = false if copy_input[t] < 0
				}
				puts "Matching in dictionary is: #{item}" if valid
			}
		}
	end

	def self.count_dict(word)
		hash = {}
		word.each_char { |letter|
			if hash[letter].nil?
				hash[letter] = 1
			else
				hash[letter] = hash[letter] + 1
			end	
		}
		hash
	end

end

String.jumble('apple', 'english-words.10')
String.jumble('dog', 'english-words.10')
String.jumble('abracadabra', 'english-words.10')

# 10:39:20-jeschen@~/Desktop/jumble ruby jumble.rb

# Input is apple
# Matching in dictionary is: a
# Matching in dictionary is: apple
# Matching in dictionary is: plea

# Input is dog
# Matching in dictionary is: do
# Matching in dictionary is: dog
# Matching in dictionary is: go

# Input is abracadabra
# Matching in dictionary is: a
# Matching in dictionary is: bad
# Matching in dictionary is: bar
# Matching in dictionary is: car
# Matching in dictionary is: card
