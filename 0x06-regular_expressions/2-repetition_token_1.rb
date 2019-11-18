#!/usr/bin/env ruby

str = ARGV[0]
str1 = str.scan(/hb?tn/).join
puts str1
