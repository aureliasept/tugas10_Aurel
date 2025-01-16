from flask import Flask, render_template, request # type: ignore

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        try:
            # Mengambil input dari form
            n = int(request.form['n'])  # Jumlah pemilih
            p = float(request.form['p'])  # Peluang memilih kandidat
            k = int(request.form['k'])  # Jumlah pemilih yang memilih kandidat
            
            # Menghitung probabilitas binomial
            result = calculate_binomial_probability(n, p, k)
        except ValueError:
            result = "Input tidak valid. Harap masukkan angka yang benar."

    return render_template('index.html', result=result)

def calculate_binomial_probability(n, p, k):
    """
    Fungsi untuk menghitung probabilitas distribusi binomial.
    Rumus: P(X = k) = C(n, k) * p^k * (1-p)^(n-k)
    """
    from math import comb
    return comb(n, k) * (p**k) * ((1-p)**(n-k))

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)
