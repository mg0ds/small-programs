import cv2
import numpy as np

#ascii_color = "@#$830O1?l!xaovcui;:>*=|^_-',. "
#ascii_color = " .,'-^!|=*:;coa?0123456789$W#@"
ascii_color = "@#W$9876543210?!aoc;:*=-,. "
#ascii_color = "qwertyuiopasdfghjklzxcvbnm"
new_txt_img = "ascii_img.txt"

#Initialize video capture
cap = cv2.VideoCapture(0)
#scaling factor
scaling_factor = 1
# Loop until you hit the Esc key
while True:
    all_pixels = []
    ascii_image = []
    bw_values = []

    # Capture the current frame
    ret, frame = cap.read()
    # Resize the frame
    frame = cv2.resize(frame, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_AREA)

    # resize video capture frame for ascii camera to match ascii character with one pixel
    scale_percent = 10  # percent of original size, 10 is best
    width = int(frame.shape[1] * scale_percent / 100)
    height = int(frame.shape[0] * scale_percent / 100)
    dim = (width, height)
    resized_frame = cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)

    # generate ascii image
    # convert one image pixel to ascii character
    for y in range(resized_frame.shape[0]):
        all_pixels.append([])
        bw_values.append([])
        new_str_line = ""
        for x in range(resized_frame.shape[1]):
            pixel = resized_frame[y, x]
            # convert RGB to black and white by averaging RGB values
            bw = int(sum(pixel) / 3)
            all_pixels[y].append(bw)
            char = ascii_color[int(bw / len(ascii_color))]
            new_str_line += char
            bw_values[y].append(str(bw))
        new_str_line += "\n"
        ascii_image.append(new_str_line)

    # blank black background for ascii camera
    empty_img = np.zeros((720, 1280, 3), dtype=np.uint8)

    # print current frame from ascii camera with black background
    y_start = 0
    x_start = 0
    font = cv2.FONT_HERSHEY_PLAIN
    font_size = 1
    font_color = (255, 255, 255)
    thick = 1
    max_row_height = int(empty_img.shape[0] / len(ascii_image))
    max_char_width = int(empty_img.shape[1] / len(ascii_image[0]))

    # resize camera window size, max_char_width and max_row_height were changed from float to int
    # so it was rounded down and lost decimal value
    empty_img = cv2.resize(empty_img, (max_char_width * len(ascii_image[0]), max_row_height * len(ascii_image)))

    for row in ascii_image:
        y_start += max_row_height
        x_start = 0

        """
        # put raw text row without any scaling on background image
        cv2.putText(empty_img, row, (0, y_start), font, font_size, font_color, thick)
        """

        # scale each character from ascii image to fixed length because ascii characters have different width
        for char in row:
            x_start += max_char_width
            # get text row width and height
            (text_width, text_height) = cv2.getTextSize(char, font, font_size, thick)[0]
            # make new shape with dimensions fixed dimension
            mask = np.zeros((max_row_height, max_char_width), dtype=np.uint8)
            # put text into new shape
            mask = cv2.putText(mask, char, (int((mask.shape[1] - text_width)/2),
                                            int((mask.shape[0] - (mask.shape[0] - text_height)/2))), font, font_size,
                               font_color, thick, cv2.LINE_8)
            # merge so it will have 3 channel
            mask = cv2.merge((mask, mask, mask))
            # combine text shape with a cut of background image (that same dimension as text shape)
            bitwise = cv2.bitwise_or(empty_img[y_start - max_row_height:y_start,
                                     x_start - max_char_width:x_start, :], mask)
            # place text shape on main image
            empty_img[y_start - max_row_height:y_start, x_start - max_char_width:x_start] = bitwise


        """
        # scale each row of text, it's faster than each character but image can be distorted
        # scale text row to fixed length because ascii characters have different width
        # get text row width and height
        (text_width, text_height) = cv2.getTextSize(row, font, font_size, thick)[0]
        # make new shape with dimensions as text
        mask = np.zeros((text_height, text_width), dtype=np.uint8)
        # put text to new shape
        mask = cv2.putText(mask, row, (0, text_height), font, font_size, font_color, thick, cv2.LINE_AA)
        # resize shape with text to match background image
        mask = cv2.resize(mask, (empty_img.shape[1], max_row_height))
        # merge so it will have 3 channel
        mask = cv2.merge((mask, mask, mask))
        # combine text shape with a cut of background image (that same dimension as text shape)
        bitwise = cv2.bitwise_or(empty_img[y_start-max_row_height:y_start, :, :], mask)
        # place text shape on main image
        empty_img[y_start-max_row_height:y_start, 0:empty_img.shape[1]] = bitwise
        """

    cv2.imshow('ASCII Webcam', empty_img)
    #cv2.imshow('Webcam', frame)

# Detect if the Esc key has been pressed
    c = cv2.waitKey(1)
    if c == 27:
        break


# Release the video capture object
cap.release()
# Close all active windows
cv2.destroyAllWindows()
