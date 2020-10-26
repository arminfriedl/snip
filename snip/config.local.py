# FLASK
FLASK_DEBUG = True
FLASK_ENV = "development"

# elisp:
# (->> (let (res) (dotimes (n 64 res) (setq res (cons (random (math-pow 2 8)) res))))
#             (--map (format "\\x%s" it))
#             (--reduce (concat acc it))
#             (kill-new))
SECRET_KEY = b'\x90\xd6\x07\xa9\x84\x41\x15\x7c\x7b\x96\xd5\xb7\xa2\x52\xc3'\
    b'\x33\x3e\x40\xdf\x0a\x64\xdc\x27\x2b\x4a\x48\x7a\x88\xf6\x4c\xce\x9a'\
    b'\x5c\x5f\xc5\xc8\xa8\xa3\xbc\x28\xc0\x10\x6d\x54\xbb\x10\x58\x86\x9c'\
    b'\x68\x1b\xcc\xad\x68\xd0\xf3\x66\x65\xb5\xf4\x70\x9d\x0e\x3d'

# SQL ALCHEMY
SQLALCHEMY_DATABASE_URI = "sqlite:////tmp/test.db"
SQLALCHEMY_TRACK_MODIFICATIONS = False
