# 🌍 **AstroView** - Advanced Asteroid Impact Risk Assessment Platform

<div align="center">

![AstroView Banner](https://img.shields.io/badge/AstroView-Asteroid%20Impact%20Simulator-green?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTEyIDJMMTMuMDkgOC4yNkwyMCA5TDEzLjA5IDE1Ljc0TDEyIDIyTDEwLjkxIDE1Ljc0TDQgOUwxMC45MSA4LjI2TDEyIDJaIiBmaWxsPSIjOUVGRjAwIi8+Cjwvc3ZnPgo=)

[![NASA Space Apps Challenge 2025](https://img.shields.io/badge/NASA%20Space%20Apps-Challenge%202025-blue?style=flat-square&logo=nasa)](https://www.spaceappschallenge.org/)
[![Built with Next.js](https://img.shields.io/badge/Built%20with-Next.js%2015-black?style=flat-square&logo=next.js)](https://nextjs.org/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.0-blue?style=flat-square&logo=typescript)](https://www.typescriptlang.org/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-3.4-06B6D4?style=flat-square&logo=tailwindcss)](https://tailwindcss.com/)

**🏆 NASA Space Apps Challenge 2025 Submission | Team Trifidia Squad**

*Advanced asteroid impact simulation and risk assessment platform designed for researchers, emergency responders, and space agencies worldwide.*

[🚀 **Live Demo**](https://astroview.space) · [📖 **Documentation**](https://docs.astroview.space) · [🐛 **Report Bug**](https://github.com/julianaivo/2025-NASA-Space-Apps-Challenge_trifidia-squad/issues) · [✨ **Request Feature**](https://github.com/julianaivo/2025-NASA-Space-Apps-Challenge_trifidia-squad/issues)

</div>

---

## 🌟 **Overview**

**AstroView** is a cutting-edge asteroid impact simulation platform that combines advanced physics modeling with intuitive visualization to assess potential asteroid threats to Earth. Built for the NASA Space Apps Challenge 2025, our platform empowers scientists, researchers, and emergency response teams with precise impact assessments and comprehensive risk analysis.

### 🎯 **Mission Statement**
*"To democratize asteroid impact risk assessment through advanced simulation technology, providing critical insights for planetary defense and emergency preparedness."*

---

## ✨ **Key Features**

### 🔬 **Advanced Physics Simulation**
- **Atmospheric Entry Modeling**: Realistic atmospheric penetration calculations
- **Fragmentation Analysis**: Multi-body breakup simulation with debris tracking
- **Energy Release Calculations**: Precise TNT-equivalent energy assessments
- **Ground Impact Physics**: Crater formation and shock wave propagation

### 🌍 **Interactive Impact Visualization**
- **Real-time 3D Mapping**: Mapbox-powered interactive Earth visualization
- **Damage Zone Visualization**: Multi-layered impact effect rendering
- **Timeline Animation**: Step-by-step impact sequence visualization
- **Risk Area Assessment**: Population and infrastructure impact analysis

### 📊 **Comprehensive Risk Dashboard**
- **Real-time KPI Monitoring**: Population at risk, economic impact, energy release
- **Threat Classification**: Automated risk level assessment
- **Historical Comparison**: Context with known impact events
- **Export Capabilities**: PDF reports and data export functionality

### 🎛️ **Professional Configuration Tools**
- **Asteroid Parameter Input**: Size, composition, velocity, and angle settings
- **Geographic Targeting**: Click-to-select impact location mapping
- **Scenario Comparison**: Multiple simulation comparison tools
- **Batch Processing**: Automated multi-scenario analysis

---

## 🛠️ **Technology Stack**

<div align="center">

| **Frontend** | **Backend** | **Mapping** | **Styling** | **Development** |
|:---:|:---:|:---:|:---:|:---:|
| ![Next.js](https://img.shields.io/badge/Next.js-15.5.4-black?style=flat-square&logo=next.js) | ![Node.js](https://img.shields.io/badge/Node.js-18+-339933?style=flat-square&logo=node.js) | ![Mapbox](https://img.shields.io/badge/Mapbox-GL%20JS-000000?style=flat-square&logo=mapbox) | ![Tailwind](https://img.shields.io/badge/Tailwind-CSS-06B6D4?style=flat-square&logo=tailwindcss) | ![TypeScript](https://img.shields.io/badge/TypeScript-5.0-3178C6?style=flat-square&logo=typescript) |
| ![React](https://img.shields.io/badge/React-18+-61DAFB?style=flat-square&logo=react) | ![API Routes](https://img.shields.io/badge/API-Routes-000000?style=flat-square) | ![OpenStreetMap](https://img.shields.io/badge/OpenStreetMap-Data-7EBC6F?style=flat-square&logo=openstreetmap) | ![Shadcn/UI](https://img.shields.io/badge/Shadcn-UI-000000?style=flat-square) | ![ESLint](https://img.shields.io/badge/ESLint-8+-4B32C3?style=flat-square&logo=eslint) |

</div>

### **Core Dependencies**
```json
{
  "next": "15.5.4",
  "react": "18.3.1",
  "typescript": "5.6.3",
  "tailwindcss": "3.4.17",
  "mapbox-gl": "latest",
  "@radix-ui/react-*": "latest",
  "lucide-react": "latest"
}
```

---

## 🚀 **Quick Start**

### **Prerequisites**
- **Node.js** 18.0 or higher
- **npm** or **pnpm** package manager
- **Mapbox Account** (for mapping functionality)

### **Installation**

```bash
# Clone the repository
git clone https://github.com/julianaivo/2025-NASA-Space-Apps-Challenge_trifidia-squad.git
cd 2025-NASA-Space-Apps-Challenge_trifidia-squad

# Install dependencies
npm install
# or
pnpm install

# Configure environment variables
cp .env.local.example .env.local
# Edit .env.local with your Mapbox token

# Start development server
npm run dev
# or
pnpm dev
```

### **Environment Configuration**
```bash
# .env.local
NEXT_PUBLIC_MAPBOX_TOKEN=your_mapbox_token_here
NEXT_PUBLIC_API_BASE_URL=https://api.astroview.space
```

### **Access the Application**
- **Development**: [http://localhost:3000](http://localhost:3000)
- **Risk Dashboard**: [http://localhost:3000/dashboard](http://localhost:3000/dashboard)
- **Impact Simulator**: [http://localhost:3000/simulador](http://localhost:3000/simulador)

---

## 📖 **Usage Guide**

### **1. Setting Up a Simulation**
1. Navigate to the **Configuration** page
2. Select impact location by clicking on the map
3. Configure asteroid parameters:
   - **Diameter**: 10m - 10km range
   - **Velocity**: 11-30 km/s
   - **Composition**: Iron, Stone, or Ice
   - **Impact Angle**: 15-90 degrees

### **2. Running Impact Analysis**
1. Click **"Run Simulation"** to execute physics calculations
2. View real-time progress and estimated completion time
3. Automatic redirect to visualization upon completion

### **3. Analyzing Results**
- **Interactive Map**: Explore damage zones and impact effects
- **Timeline View**: Step-through impact sequence
- **Risk Dashboard**: Review population and economic impact
- **Export Options**: Generate PDF reports or export raw data

---

## 🔬 **Scientific Methodology**

### **Physics Models**
Our simulation engine implements peer-reviewed scientific models:

- **Atmospheric Entry**: [Collins et al. (2005)](https://doi.org/10.1111/j.1945-5100.2005.tb00157.x) atmospheric breakup model
- **Ground Impact**: [Melosh (1989)](https://doi.org/10.1093/oso/9780195103731.001.0001) impact cratering mechanics
- **Blast Effects**: [Glasstone & Dolan (1977)](https://www.fourmilab.ch/etexts/www/effects/) nuclear weapons effects scaling
- **Population Assessment**: Integration with OpenStreetMap demographic data

### **Validation**
All calculations are validated against:
- **Tunguska Event (1908)**: Atmospheric airburst simulation
- **Chelyabinsk Event (2013)**: Modern impact validation
- **Meteor Crater (Arizona)**: Ground impact verification

---

<div align="center">

### **🌍 Interactive Impact Simulator**
*Real-time visualization of asteroid impact effects with multi-layered damage zones*

### **📊 Risk Assessment Dashboard**
*Comprehensive KPI monitoring and threat classification system*

### **⚙️ Advanced Configuration Interface**
*Professional-grade parameter input and scenario management*

</div>

---

## 🤝 **Contributing**

We welcome contributions from the scientific community, developers, and space enthusiasts!

### **Development Setup**
```bash
# Fork the repository
git clone https://github.com/your-username/2025-NASA-Space-Apps-Challenge_trifidia-squad.git

# Create feature branch
git checkout -b feature/amazing-feature

# Make your changes and commit
git commit -m "Add amazing feature"

# Push to branch
git push origin feature/amazing-feature
```
---

</div>

---

## 🙏 **Acknowledgments**

- **NASA** for hosting the Space Apps Challenge and providing inspiration
- **Mapbox** for excellent mapping infrastructure
- **OpenStreetMap** community for geographic data
- **Vercel** for hosting and deployment platform
- **Scientific Community** for validated impact models
- **Open Source Community** for amazing tools and libraries

---

<div align="center">

**⭐ If you find AstroView useful, please consider giving us a star on GitHub! ⭐**

[![GitHub stars](https://img.shields.io/github/stars/julianaivo/2025-NASA-Space-Apps-Challenge_trifidia-squad?style=social)](https://github.com/julianaivo/2025-NASA-Space-Apps-Challenge_trifidia-squad)

---

*Built with ❤️ for planetary defense and space science education*

**© 2025 Team Trifidia Squad | NASA Space Apps Challenge**

</div>
