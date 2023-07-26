ffmpeg -i 0.mp4 -c copy -bsf:v h264_mp4toannexb -f mpegts temp0.ts
ffmpeg -i 1.mp4 -c copy -bsf:v h264_mp4toannexb -f mpegts temp1.ts
ffmpeg -i 2.mp4 -c copy -bsf:v h264_mp4toannexb -f mpegts temp2.ts
ffmpeg -i 3.mp4 -c copy -bsf:v h264_mp4toannexb -f mpegts temp3.ts
ffmpeg -i 4.mp4 -c copy -bsf:v h264_mp4toannexb -f mpegts temp4.ts
ffmpeg -i 5.mp4 -c copy -bsf:v h264_mp4toannexb -f mpegts temp5.ts
ffmpeg -i 6.mp4 -c copy -bsf:v h264_mp4toannexb -f mpegts temp6.ts
ffmpeg -i 7.mp4 -c copy -bsf:v h264_mp4toannexb -f mpegts temp7.ts
ffmpeg -i 8.mp4 -c copy -bsf:v h264_mp4toannexb -f mpegts temp8.ts
ffmpeg -i 9.mp4 -c copy -bsf:v h264_mp4toannexb -f mpegts temp9.ts
ffmpeg -i 10.mp4 -c copy -bsf:v h264_mp4toannexb -f mpegts temp10.ts



ffmpeg -i "concat:temp0.ts|temp1.ts|temp2.ts|temp3.ts|temp4.ts|temp5.ts|temp6.ts|temp7.ts|temp8.ts|temp9.ts|temp10.ts" -c copy -bsf:a aac_adtstoasc O.mp4