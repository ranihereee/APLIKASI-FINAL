import streamlit as st
import math

st.markdown("<h1 style='text-align: center; color: blue;'>ISOKINETIC PRESENTAGE</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: black;'>digunakan untuk memudahkan kalian menghitung persen isokinetik untuk menguji kadar partikulat emisi sumber tidak bergerak </h2>", unsafe_allow_html=True)
st.caption('Alat ini dibuat oleh anggota kelompok 7 yaitu Akbar Kurnia ramadhan,Deby marsha,Kurnia Aynun,Nathalia,dan muhammad fauzi untuk keperluan tugas mata kuliah logika pemrograman komputer.')
st.caption('**alat ini masih dalam versi percobaan**')
st.write('untuk memulai perhitungan silahkan tekan tombol garis tiga di kiri atas untuk berpindah portal')
st.markdown("<hr style='height:1px;border:none;color:#333;background-color:#333;' />", unsafe_allow_html=True)


menu = ["home", "kalkulator", "panduan perhitungan"]
choice = st.sidebar.selectbox("PORTAL", menu)
if choice == "home":
    st.write("Ini adalah halaman kontak")

    def main():

        st.title("Sampling Isokinetik")
        st.header("Metode Pengambilan Sampel udara emisi dengan cara isokinetik")

        st.markdown(
        """
        ![Isokinetic Sampling](https://yellowtree.co.za/wp-content/uploads/2019/01/Testing-of-a-Process-Stack.png)

        *Gambar ilustrasi proses sampling isokinetik*

        Sampling isokinetik adalah metode pengambilan contoh atau sampel dari aliran fluida dengan kecepatan konstan. 
        Metode ini digunakan untuk mengambil sampel udara, gas, atau partikel padat dalam suatu sistem dengan mempertahankan kecepatan aliran yang konsisten di seluruh proses pengambilan sampel.

        Tujuan dari sampling isokinetik adalah untuk mendapatkan sampel yang mewakili komposisi dan konsentrasi yang sebenarnya dari suatu zat dalam aliran fluida. 
        Metode ini sering digunakan dalam industri dan lingkungan untuk mengukur emisi gas buang dari cerobong asap, evaluasi kualitas udara dalam ruangan, serta untuk mengambil sampel partikel debu atau serbuk dalam industri pengolahan.

        Proses sampling isokinetik melibatkan penggunaan alat pengambilan sampel khusus yang disebut probe isokinetik. 
        Probe ini dirancang untuk menciptakan kondisi aliran yang isokinetik dengan menghasilkan kecepatan aliran yang sama dengan kecepatan aliran alami fluida yang akan disampel.

        Kecepatan aliran yang dihasilkan oleh probe isokinetik diatur sedemikian rupa sehingga partikel yang terdapat dalam fluida akan didistribusikan secara proporsional dalam sampel yang diambil.

        Proses pengambilan sampel isokinetik juga melibatkan pemantauan dan pengendalian parameter seperti kecepatan aliran fluida, tekanan, suhu, dan faktor-faktor lainnya yang dapat mempengaruhi hasil sampling. 
        Dengan menjaga kecepatan aliran yang konstan, metode ini memungkinkan penentuan konsentrasi yang akurat dan representatif dari zat yang sedang diukur.

        Sampling isokinetik penting dalam pengujian emisi untuk memastikan kepatuhan terhadap peraturan lingkungan yang ada. 
        Metode ini juga digunakan dalam penelitian dan pemantauan lingkungan untuk mengukur kualitas udara dan kadar partikel yang berpotensi berbahaya bagi kesehatan manusia.

        Secara keseluruhan, sampling isokinetik adalah metode yang digunakan untuk mengambil sampel fluida dengan kecepatan aliran yang konstan, sehingga mewakili komposisi dan konsentrasi yang sebenarnya dari zat yang ingin diukur. 
        Metode ini penting dalam pengujian emisi, penelitian lingkungan, dan evaluasi kualitas udara.
        """
        )

    if __name__ == "__main__":
        main()

elif choice == "kalkulator":
    st.markdown("<h2 style='color: blue;'>PERHITUNGAN PARTIKULAT SECARA ISOKINETIK</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: black;'>Mulai menghitung yukk ", unsafe_allow_html=True)
    d = st.number_input('Diameter Saluran Gas (m)', value=0.5, step=0.1)
    v = st.number_input('Kecepatan Gas (m/s)', value=10, step=1)
    rho = st.number_input('Densitas Gas (kg/m3)', value=1.2, step=0.1)
    c = st.number_input('Konsentrasi Partikel Dalam Gas (mg/m3)', value=100, step=10)
    A = math.pi/4 * d**2
    Q = A * v
    C = c / 1000000
    massa = Q * rho * C
    massa_total = Q * c / 1000
    efisiensi = (massa_total - massa) / massa_total * 100
   
    if st.button('Hitung'):
        # Output hasil perhitungan
        st.write('## Hasil Perhitungan')
        col1, col2, col3 = st.columns(3)
        col1.metric('Laju Aliran Gas (m3/s)', f'{Q:.2f}')
        col2.metric('Massa Debu Terbawa oleh Gas (kg)', f'{massa:.4f}')
        col3.metric('Massa Total Debu yang Terukur (mg)', f'{massa_total:.2f}')
        st.write(f"Efisiensi Pengendapan Debu = {efisiensi:.2f}%")


else:

    st.title("Penjelasan Sampling Isokinetik")

    st.markdown(
        """
        <style>
        .big-font {
            font-size: 24px !important;
        }
        .highlight {
            background-color: #FDE8E8;
            padding: 10px;
            border-radius: 5px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<p class='big-font'>Hai semuanya!</p>", unsafe_allow_html=True)
    st.write("Apakah kalian pernah mendengar tentang sampling isokinetik? Ini adalah metode pengambilan sampel yang digunakan untuk mengukur laju aliran gas atau cairan pada suatu sistem.")

    st.markdown("<p class='big-font'>Tapi, kenapa disebut isokinetik?</p>", unsafe_allow_html=True)
    st.write("Karena metode ini memastikan bahwa laju aliran gas atau cairan yang diambil adalah konstan dan sebanding dengan laju aliran aktual dalam sistem.")

    st.markdown("<p class='big-font'>Bagaimana cara melakukan sampling isokinetik?</p>", unsafe_allow_html=True)
    st.write("Kita perlu menggunakan peralatan yang disebut dengan **sampler isokinetik**. Peralatan ini bekerja dengan cara mengatur kecepatan aliran sampel yang diambil agar sama dengan kecepatan aliran aktual dalam sistem.")

    st.markdown("<p class='highlight'>Dengan begitu, sampel yang diambil akan mewakili kondisi aliran aktual dalam sistem.</p>", unsafe_allow_html=True)
    st.write("Metode sampling isokinetik ini biasa digunakan dalam berbagai aplikasi seperti pengukuran emisi gas buang, evaluasi kualitas udara dalam ruangan, dan sebagainya.")

    st.markdown("<p class='big-font'>Jadi, itu dia penjelasan singkat tentang sampling isokinetik.</p>", unsafe_allow_html=True)
    st.write("Semoga bermanfaat dan tentunya lucu! Terima kasih sudah membaca!")

    st.write('## Rumus Perhitungan')
    st.latex(r'''
        A = \frac{\pi}{4} d^2
    ''')
    st.latex(r'''
        Q = A v
    ''')
    st.write('di mana Q adalah laju aliran gas atau cairan (m^3/s).')
    st.write('A adalah luas penampang saluran gas atau cairan (m^2).')
    st.write('v adalah kecepatan gas atau cairan (m/s).')
    st.write('d adalah diameter yang sudah diinput di atas.')
    st.latex(r'''
        C = \frac{c}{10^6}
    ''')
    st.write('''di mana:
    C adalah konsentrasi partikel dalam gas (kg/m^3).
    c adalah konsentrasi partikel dalam gas (mg/m^3).''')
    st.latex(r'''
        massa = Q \rho C
    ''')
    st.latex(r'''
        massa_{total} = Q \frac{c}{1000}
    ''')


