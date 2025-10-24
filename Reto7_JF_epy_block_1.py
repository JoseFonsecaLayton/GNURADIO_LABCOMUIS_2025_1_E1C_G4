import numpy as np
from gnuradio import gr

class blk(gr.sync_block):
    """
    Bloque que calcula la media y desviación estándar de la magnitud
    sobre una ventana de tamaño vlen, iterando sobre una secuencia compleja continua.
    """
    def __init__(self, vlen=1024):
        gr.sync_block.__init__(
            self,
            name='Estadísticas de Amplitud (stream)',
            in_sig=[np.complex64],            # entrada continua (no vector)
            out_sig=[np.float32, np.float32]  # salidas escalares
        )
        self.vlen = int(vlen)
        self.buffer = np.array([], dtype=np.complex64)

    def work(self, input_items, output_items):
        in0 = input_items[0]
        out_mean = output_items[0]
        out_std  = output_items[1]

        # Agregamos las nuevas muestras al buffer
        self.buffer = np.concatenate((self.buffer, in0))

        n_out = 0
        # Mientras tengamos suficientes muestras para una ventana
        while len(self.buffer) >= self.vlen:
            # Tomamos una ventana
            window = self.buffer[:self.vlen]

            # Calculamos magnitudes
            mags = np.abs(window)

            # Calculamos estadísticos
            mean_val = np.mean(mags)
            std_val  = np.std(mags)

            # Guardamos los resultados en las salidas
            out_mean[n_out] = mean_val
            out_std[n_out]  = std_val
            n_out += 1

            # Desplazamos la ventana (no solapada)
            self.buffer = self.buffer[self.vlen:]

        return n_out

