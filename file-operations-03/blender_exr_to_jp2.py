import bpy
import os
import sys

def decodeName(name):
	file = os.path.basename(name)
	name, ext = file.split(".")

	i = len(name) - 1
	start = ""
	length = 0
	while i >= 0 and name[i] in "0123456789":
		start = name[i] + start
		i -= 1
		length += 1

	prefix = name[:i + 1]

	return (prefix, length, int(start))

def main():
	first_frame = sys.argv[-2]
	output_dir = sys.argv[-1]

	#first_frame = "/home/sergey/tmp/17/movie/MMI_2366_00000.jpg"
	#first_frame = "/home/sergey/tmp/17/movie2/04_2e_0012.exr"
	#output_dir = "/tmp/export"

	if not output_dir.endswith("/"):
		output_dir += "/"

	prefix, length, start = decodeName(first_frame)

	output_dir += prefix + ("#" * length)

	context = bpy.context
	scene = context.scene

	scene.sequence_editor_clear()
	scene.sequence_editor_create()

	clip = bpy.data.movieclips.load(first_frame)

	seq = scene.sequence_editor.sequences.new_clip(name="Clip",
													clip=clip,
													channel=1,
													start_frame=start)

	scene.sequencer_colorspace_settings.name = 'Raw'
	
	#scene.render.resolution_x = clip.size[0]
	#scene.render.resolution_y = clip.size[1]
	
	scene.render.resolution_x = 2048
	scene.render.resolution_y = 1080
	scene.frame_current = start
	scene.frame_start = start
	scene.frame_end = start + clip.frame_duration - 2
	scene.render.use_sequencer = True
	scene.render.resolution_percentage = 100

	scene.render.image_settings.file_format = 'JPEG2000'
	scene.render.image_settings.color_depth = '8'
	scene.render.image_settings.quality = 70
	scene.render.filepath = output_dir

	bpy.ops.render.render(animation=True)

if __name__ == "__main__":
	main()
