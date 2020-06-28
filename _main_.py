import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as mpatches
from mpl_toolkits.mplot3d import axes3d
from matplotlib import style
import numpy as np
import math
import time

#plt.style.use('dark_background')
class ParticleInABox():

    class OneDimensional():

        def __init__(self, length_x, quantum_number, time_dependence):

            self.length_x = length_x
            self.quantum_number = quantum_number
            self.time_dependence = time_dependence

        def wavefunction(self):
            if self.time_dependence == True:

                figure = plt.figure()
                figure.show()

                """Generate time intervals."""
                t = []
                for i in range(0, 1000):
                    u = i*100
                    t.append(u)

                for time_interval in t:
                    plt.clf()
                    axis = figure.add_subplot(111)
                    axis.autoscale(False)
                    plt.xlim(0, self.length_x)
                    plt.ylim(-1.5, 1.5)
                    
                    x = []
                    for i in range((self.length_x)*100):
                        u = i/100
                        x.append(u)
        
                    real_y = []
                    imaginary_y = [] 

                    for i in x:
                        real_output = math.cos((pow(self.quantum_number, 2)*6.626*pow(10, -34)*math.pi*time_interval)/(4*9.109*pow(10, -31)*self.length_x))*math.sqrt((2)/(self.length_x))*math.sin((math.pi*self.quantum_number*i)/(self.length_x))
                        imaginary_output = -1*math.sin((pow(self.quantum_number, 2)*6.626*pow(10, -34)*math.pi*time_interval)/(4*9.109*pow(10, -31)*self.length_x))*math.sqrt((2)/(self.length_x))*math.sin((math.pi*self.quantum_number*i)/(self.length_x))
                        real_y.append(real_output)
                        imaginary_y.append(imaginary_output)

                    axis.plot(x, real_y, color = "blue", label = r'$Re[\psi(x)$]')
                    axis.plot(x, imaginary_y, color = "red", label = r'$Im[\psi(x)]$')
                    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left', ncol=2, mode="expand", borderaxespad=0.)
                    axis.set_xlabel(r'$x$')
                    figure.canvas.draw()
                    time.sleep(0.01)

            else:
                x = []
                for i in range((self.length_x)*100):
                    u = i/100
                    x.append(u)
        
                y = []

                for i in x:
                    output = math.sqrt((2)/(self.length_x))*math.sin((math.pi*self.quantum_number*i)/(self.length_x))
                    y.append(output)

                plt.plot(x, y)
                plt.show()

        def PDF(self):

            if self.time_dependence == True:

                figure = plt.figure()
                figure.show()

                """Generate time intervals."""
                t = []
                for i in range(0, 1000):
                    u = i*100
                    t.append(u)

                for time_interval in t:
                    plt.clf()
                    axis = figure.add_subplot(111)
                    axis.autoscale(False)
                    plt.xlim(0, self.length_x)
                    plt.ylim(-1.5, 1.5)
                    
                    x = []
                    for i in range((self.length_x)*100):
                        u = i/100
                        x.append(u)
        
                    y = []

                    for i in x:
                        output = math.exp(-1*(pow(self.quantum_number, 2)*6.626*pow(10, -34)*math.pi*time_interval)/(4*9.109*pow(10, -31)*self.length_x))*(2/self.length_x)*pow(math.sin((math.pi*self.quantum_number*i)/(self.length_x)), 2)
                        y.append(output)

                    axis.plot(x, y, color = "blue")
                    axis.set_xlabel(r'$x$')
                    axis.set_ylabel(r'$|\psi(x)|^2$')
                    figure.canvas.draw()
                    time.sleep(0.01)

            else:

                x = []
                for i in range((self.length_x)*100):
                    u = i/100
                    print(u)
                    x.append(u)

                y = []

                for i in x:
                    output = (2/self.length_x)*pow(math.sin((math.pi*self.quantum_number*i)/(self.length_x)), 2)
                    y.append(output)

                plt.plot(x, y)
                plt.xlabel('\\alpha')
                plt.ylabel('\\beta')
                plt.show()

    class TwoDimensional():

        def __init__(self, length_x, length_y, quantum_number_x, quantum_number_y):

            self.length_x = length_x
            self.length_y = length_y
            self.quantum_number_x = quantum_number_x
            self.quantum_number_y = quantum_number_y

        def wavefunction(self):

            """Generating x-coordinates."""
            x = np.linspace(0, self.length_x, 100)

            """Generating y-coordinates."""
            y = np.linspace(0, self.length_y, 100)

            """Generating all possible xy-coordinates."""
            X,Y = np.meshgrid(x,y)

            """Generating z-coordinates from xy-coordinates."""
            Z = np.sqrt((2)/(self.length_x*self.length_y))*np.sin((math.pi*self.quantum_number_x*X)/(self.length_x))*np.sin((math.pi*self.quantum_number_y*Y)/(self.length_y))

            """Generating plot."""
            figure = plt.figure()
            axis = figure.gca(projection='3d')
            contour = axis.plot_surface(X,Y,Z,cmap='hot')
            figure.colorbar(contour, shrink = 0.75)
            axis.set_xlabel(r'$x$')
            axis.set_ylabel(r'$y$')
            axis.set_zlabel(r'$\psi(x, y)$')
            axis.view_init(elev = 30, azim = -135)
            plt.show()

        def PDF(self):

            """Generating x-coordinates."""
            x = np.linspace(0, self.length_x, 1000)

            """Generating y-coordinates."""
            y = np.linspace(0, self.length_y, 1000)

            """Generating all possible xy-coordinates."""
            X,Y = np.meshgrid(x,y)

            """Generating z-coordinates from xy-coordinates."""
            Z = (2/self.length_x*self.length_y)*pow(np.sin((math.pi*self.quantum_number_x*X)/(self.length_x))*np.sin((math.pi*self.quantum_number_y*Y)/(self.length_y)),2)

            """Generating plot."""
            figure = plt.figure()
            axis = figure.gca(projection='3d')
            contour = axis.plot_surface(X,Y,Z,cmap='hot')
            figure.colorbar(contour, shrink = 0.75)
            axis.set_xlabel(r'$x$')
            axis.set_ylabel(r'$y$')
            axis.set_zlabel(r'$|\psi(x, y)|^2$')
            axis.view_init(elev = 30, azim = -135)
            plt.show()

    class ThreeDimensional():

        def __init__(self, length_x, length_y, length_z, quantum_number_x, quantum_number_y, quantum_number_z, scatter_density):

            self.length_x = length_x
            self.length_y = length_y
            self.length_z = length_z
            self.quantum_number_x = quantum_number_x
            self.quantum_number_y = quantum_number_y
            self.quantum_number_z = quantum_number_z
            self.scatter_density = scatter_density

        def wavefunction(self):

            """Generating x-coordinates."""
            x = []
            for i in range((self.length_x)*self.scatter_density):
                u = i/self.scatter_density
                x.append(u)

            """Generating y-coordinates."""
            y = []
            for i in range((self.length_y)*self.scatter_density):
                u = i/self.scatter_density
                y.append(u)

            """Generating z-coordinates."""
            z = []
            for i in range((self.length_z)*self.scatter_density):
                u = i/self.scatter_density
                z.append(u)

            """Generating all possible xyz-coordinates."""
            space_coordinates = []
            counter = 0
            for i in x:
                for j in y:
                    for k in z:
                        coordinate = []
                        coordinate.append(i)
                        coordinate.append(j)
                        coordinate.append(k)
                        space_coordinates.append(coordinate)
                        counter = counter + 1

            """Generating colour-coordinates from xyz-coordinates."""
            for coordinate in space_coordinates:
                output = math.sqrt((2)/(self.length_x*self.length_y*self.length_z))*math.sin((math.pi*self.quantum_number_x*coordinate[0])/(self.length_x))*math.sin((math.pi*self.quantum_number_y*coordinate[1])/(self.length_y))*math.sin((math.pi*self.quantum_number_z*coordinate[2])/(self.length_z))
                coordinate.append(output)

            """Formatting colour-xyz-coordinates."""
            x_plot = []
            y_plot = []
            z_plot = []
            colour_plot = []
            for coordinate in space_coordinates:
                x_plot.append(coordinate[0])
                y_plot.append(coordinate[1])
                z_plot.append(coordinate[2])
                colour_plot.append(coordinate[3])

            """Generating plot"""
            fig = plt.figure()
            ax1 = fig.add_subplot(111, projection='3d')
            img = ax1.scatter(x_plot, y_plot, z_plot, c=colour_plot, cmap=plt.get_cmap('jet'))
            fig.colorbar(img)
            ax1.set_xlabel(r'$x$')
            ax1.set_ylabel(r'$y$')
            ax1.set_zlabel(r'$|\psi(x, y)|^2$')
            plt.show()

        def PDF(self):

            """Generating x-coordinates."""
            x = []
            for i in range((self.length_x)*self.scatter_density):
                u = i/self.scatter_density
                x.append(u)

            """Generating y-coordinates."""
            y = []
            for i in range((self.length_y)*self.scatter_density):
                u = i/self.scatter_density
                y.append(u)

            """Generating z-coordinates."""
            z = []
            for i in range((self.length_z)*self.scatter_density):
                u = i/self.scatter_density
                z.append(u)

            """Generating all possible xyz-coordinates."""
            space_coordinates = []
            counter = 0
            for i in x:
                for j in y:
                    for k in z:
                        coordinate = []
                        coordinate.append(i)
                        coordinate.append(j)
                        coordinate.append(k)
                        space_coordinates.append(coordinate)
                        counter = counter + 1

            """Generating colour-coordinates from xyz-coordinates."""
            for coordinate in space_coordinates:
                output = (2/(self.length_x*self.length_y*self.length_z))*pow(math.sin((math.pi*self.quantum_number_x*coordinate[0])/(self.length_x))*math.sin((math.pi*self.quantum_number_y*coordinate[1])/(self.length_y))*math.sin((math.pi*self.quantum_number_z*coordinate[2])/(self.length_z)),2)
                coordinate.append(output)

            """Formatting colour-xyz-coordinates."""
            x_plot = []
            y_plot = []
            z_plot = []
            colour_plot = []
            for coordinate in space_coordinates:
                x_plot.append(coordinate[0])
                y_plot.append(coordinate[1])
                z_plot.append(coordinate[2])
                colour_plot.append(coordinate[3])

            """Generating plot"""
            fig = plt.figure()
            ax1 = fig.add_subplot(111, projection='3d')
            img = ax1.scatter(x_plot, y_plot, z_plot, c=colour_plot, cmap=plt.get_cmap('jet'))
            fig.colorbar(img)
            ax1.set_xlabel(r'$x$')
            ax1.set_ylabel(r'$y$')
            ax1.set_zlabel(r'$z$')
            plt.title(r'$|\psi(x, y, z)|^{2}$')
            plt.show()

ParticleInABox().OneDimensional(length_x = 1, quantum_number = 2, time_dependence = True).PDF()
