#!/usr/bin/env ruby

str = ARGV[0]
str1 = str.scan(/hbt+n/).join
puts str1
