# from flask import Flask, render_template, request

# app = Flask(__name__)

# @app.route("/", methods=["GET", "POST"])
# def index():
#     if request.method == "POST":
#         pages = list(map(int, request.form["pages"].strip().split()))
#         frame_size = int(request.form["frame_size"])

#         frames = []
#         matrix = []
#         status_list = []
#         page_faults = 0

#         for page in pages:
#             status = "HIT" if page in frames else "MISS"
#             if status == "MISS":
#                 page_faults += 1
#                 if len(frames) < frame_size:
#                     frames.append(page)
#                 else:
#                     frames.pop(0)
#                     frames.append(page)
#             # Build matrix column-wise
#             column = []
#             for i in range(frame_size):
#                 if i < len(frames):
#                     column.append(frames[i])
#                 else:
#                     column.append("")
#             matrix.append(column)
#             status_list.append(status)

#         result = {
#             "pages": pages,
#             "steps": len(pages),
#             "frame_size": frame_size,
#             "matrix": matrix,
#             "status_list": status_list,
#             "faults": page_faults
#         }

#         return render_template("index.html", result=result)

#     return render_template("index.html", result=None)

# if __name__ == "__main__":
#     app.run(debug=True)


from flask import Flask, render_template, request

app = Flask(__name__)

# FIFO Algorithm (Already Implemented)
def fifo_page_replacement(pages, frame_size):
    frames = []
    matrix = []
    status_list = []
    page_faults = 0

    for page in pages:
        status = "HIT" if page in frames else "MISS"
        if status == "MISS":
            page_faults += 1
            if len(frames) < frame_size:
                frames.append(page)
            else:
                frames.pop(0)  # FIFO: pop the first element
                frames.append(page)
        # Build matrix column-wise
        column = []
        for i in range(frame_size):
            if i < len(frames):
                column.append(frames[i])
            else:
                column.append("")
        matrix.append(column)
        status_list.append(status)
    
    return matrix, status_list, page_faults

# LRU Algorithm Implementation
def lru_page_replacement(pages, frame_size):
    frames = []
    matrix = []
    status_list = []
    page_faults = 0

    for page in pages:
        status = "MISS"
        
        # If the page is already in memory, it is a HIT
        if page in frames:
            status = "HIT"
            frames.remove(page)  # Remove the page if it is already in memory
            frames.append(page)   # Add it to the most recent position (end of the list)
        else:
            # Page fault occurred
            status = "MISS"
            page_faults += 1
            if len(frames) < frame_size:
                frames.append(page)  # If there is space, add the page
            else:
                frames.pop(0)  # If the frame is full, remove the least recently used page
                frames.append(page)  # Add the new page
        
        # Build matrix column-wise for visualization
        column = []
        for i in range(frame_size):
            if i < len(frames):
                column.append(frames[i])
            else:
                column.append("")
        matrix.append(column)
        status_list.append(status)

    return matrix, status_list, page_faults

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        pages = list(map(int, request.form["pages"].strip().split()))
        frame_size = int(request.form["frame_size"])
        algorithm = request.form.get("algorithm")

        if algorithm == "LRU":
            matrix, status_list, page_faults = lru_page_replacement(pages, frame_size)
        else:  # Default to FIFO
            matrix, status_list, page_faults = fifo_page_replacement(pages, frame_size)

        result = {
            "pages": pages,
            "steps": len(pages),
            "frame_size": frame_size,
            "matrix": matrix,
            "status_list": status_list,
            "faults": page_faults,
            "algorithm": algorithm
        }

        return render_template("index.html", result=result)

    return render_template("index.html", result=None)

if __name__ == "__main__":
    app.run(debug=True)
