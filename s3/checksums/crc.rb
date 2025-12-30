require 'zlib'
crc32 = Zlib.crc32(File.read(ARGV[0]))
puts crc32.to_s(16).rjust(8, '0')