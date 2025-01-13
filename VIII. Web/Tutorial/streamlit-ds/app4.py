import streamlit as st
import matplotlib.pyplot as plt

st.title('Line plot with Matplotlib')

# Data
years = [1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020]
population = [2.5, 3.0, 3.7, 4.5, 5.3, 6.1, 6.9, 7.7]
population2 = [7.7, 8.1, 8.5, 9.0, 9.5, 10.0, 10.5, 11.0]

# Create plot
# Here we define fig and ax and subsequently replace plt by ax for the plots
fig, ax = plt.subplots()

ax.plot(years, population, 'r--')
ax.scatter(years, population, c='r', alpha=0.6)

ax.plot(years, population2, 'g')
ax.scatter(years, population2, c='g', alpha=0.6)

# Add labels
plt.title('Population Growth')
plt.xlabel('Year')
plt.ylabel('Population (millions)')

# Show plot
# Instead of plt.show() we're using st.pyplot
st.pyplot(fig)
