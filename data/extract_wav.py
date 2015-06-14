import sys
import struct
import wave

def usage():
    print "Usage: %s <input> <output>" % sys.argv[0]
    print "Input must be an 8-bit mono WAV file."

if len(sys.argv) != 3:
    usage()
else:
    inf = wave.open(sys.argv[1], "rb")
    outf = open(sys.argv[2], "wb")

    channels = inf.getnchannels()
    depth = inf.getsampwidth()
    size = inf.getnframes()
    if channels != 1 or depth != 1:
        usage()

    wavdata = inf.readframes(size)
    inf.close()
    outf.write(wavdata)
    outf.close()
