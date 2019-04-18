![logo](img/LogoPage.png)
In this repository, we are sharing some of the tools we used in our paper, and we hope they will enable in creating more immersive virtual reality video experiences. This repository is for open source codes and materials for the IEEE Journal on Emerging and Selected Topics in Circuits and Systems: Special issue on Immersive Video Coding and Transmission: Visual Attention-Aware Omnidirectional Video Streaming Using Optimal Tiles for Virtual Reality

### Abstract
Owing to its interactive look around nature and very large resolution requirement, providing immersive *omnidirectional video* (ODV) streaming experiences in *virtual reality* (VR) applications demands cost-effective solutions to meet both the content delivery network and device constraints. In this paper, we introduce an adaptive omnidirectional video (ODV) streaming pipeline that optimizes DASH representations of ODV content considering their visual attention (VA) maps. The main contribution of this paper is the use of VA maps: (*i*) to compute a novel objective quality metric that captures the fact that not all of the ODV is actually watched by users: the visual attention spherical weighted (VASW)-based objective quality measurement, (*ii*) to define optimal tile representations of the ODV frames, namely tiling schemes, which are composed of variable-sized and non-overlapping tiles, and (*iii*) to efficiently distribute a given bitrate budget among the set of tiles within a tiling scheme for an ODV. We evaluate the proposed system performance with varying bandwidth conditions and the tracked head orientations from user experiments. Results show that the proposed system significantly outperforms the existing non-tiled and tile-based streaming solutions.

### Downloads
[Paper](https://v-sense.scss.tcd.ie/wp-content/uploads/2019/03/JETCAS_SI_immersive_2018_pc.pdf)

[Tiling Schemes](https://github.com/cozcinar/optimalTiles/blob/master/tilingSchemes.zip) with a python script (codes/visualizeStructure.py) to visualize tiling schemes

DataSet: Visual Attention (will be available soon)

### Citation

| Paper accepted in [IEEE Journal on Emerging and Selected Topics in Circuits and Systems: Special issue on Immersive Video Coding and Transmission ](https://ieeexplore.ieee.org/xpl/tocresult.jsp?isnumber=8664408) |

Please cite our [paper](https://v-sense.scss.tcd.ie/wp-content/uploads/2019/03/JETCAS_SI_immersive_2018_pc.pdf) in your publications if it helps your research:
````
@inproceedings{streamingVAODV,
author={C. {Ozcinar} and J. {Cabrera} and A. {Smolic}}, 
journal={IEEE Journal on Emerging and Selected Topics in Circuits and Systems}, 
title={Visual Attention-Aware Omnidirectional Video Streaming Using Optimal Tiles for Virtual Reality}, 
year={2019}, 
volume={9}, 
number={1}, 
pages={217-230}, 
keywords={Streaming media;Bit rate;Encoding;Visualization;Distortion;Optimization;Pipelines;Omnidirectional video;visual attention;tiles;adaptive streaming;virtual reality}, 
doi={10.1109/JETCAS.2019.2895096}, 
ISSN={2156-3357}, 
month={March}
}
````

### Authors

| [Cagri Ozcinar][CagriOzcinar-web] | [Julian Cabrera][JulianCabrera-web] | [Aljosa Smolic][AljosaSmolic-web] |

[CagriOzcinar-web]: (https://www.scss.tcd.ie/~ozcinarc/)

[JulianCabrera-web]: (http://www.gti.ssr.upm.es/julian-cabrera)

[AljosaSmolic-web]: (https://v-sense.scss.tcd.ie/?profile=prof-aljosa-smolic-2)

### Acknowledgement

This publication has emanated from research conducted with the financial support of Science Foundation Ireland (SFI) under the Grant Number 15/RP/2776. This work has also been partially supported by the Ministerio de Econom\'ia, Industria y Competitividad (AEI/FEDER) of the Spanish Government under project TEC2016-75981 (IVME).

### Contact

If you have any question, send an e-mail at [ozcinarc@scss.tcd.ie]()
