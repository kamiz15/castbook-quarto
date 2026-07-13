### Chu et al. (2004)

This is 2D horizontal model and provides an estimate of a steady-state plume length ($L_{max}$) and investigates the large-time solution behavior of a representative bio-reactive transport model under the conditions that the mixing of two required substrate occurs only in the directions transverse to groundwater flow.

Chu et al. (2004) provides the following explicit expression for $L_{max}$:
$$
L_{max} = \frac{\pi}{16}\frac{W^2}{\alpha_{TH}}\bigg(\frac{\gamma C_{ED}^\circ}{C_{EA}^\circ+\epsilon}\bigg)^2
$$
$W$ = Source Width [L]
$\alpha_{TH}$ = Horizontal Transverse Dispersivity [L]
$\gamma$ = Reaction stoichiometric ratio [ ]
$C_{ED}^\circ$ = Contaminant (Electron Donor) concentration [ML$^{-3}$]
$C_{EA}^\circ$ = Partner Reactant (Electron Acceptor) concentration [ML$^{-3}$]

$\epsilon$ = Biological concentration factor [ML$^{-3}$]

**The model is based on the following assumptions:**

1. There is a continuous line source of contamination and instantaneous reaction model.
2. A dissolved contaminant is assumed to be biodegraded only at its plume fringe because of transverse mixing but not inside the plume.

#### Reference:

M. Chu P. K. Kitanidis P. L. McCarty. Modeling microbial reactions at the plume fringe subject to transverse mixing in porous media: When can the rates of microbial reaction be assumed to be instantaneous? https://doi.org/10.1029/2004WR003495

### Using Chu et al. (2004) model in CAST

### Single computing interface

The CAST user-interface for all the analytical models are identical. This is true for both single computing interface and multiple simulation interface. The identical interface simplifies the use of models in the CAST. Therefore, the extensive details on using the [Liedl et al. (2005)](refli2005) model in CAST provided [here](refli) can be used also for the Chu et al. (2004).

The difference in each model interface is the model specific parameters. This can be observed in the CAST screenshot below: 

Image chu2004_1:

Once the input data is placed in the box, user needs to click on the **`Generate Graph`** to get the result. Results are obtained as an absolute number below the Generate Graph button and also graphically, which provides the field plume length data from the database. This allows a visual comparison of the model $L_{max}$with the field data.



As explained in detail in [Liedl et al. (2005)](refli2005) model , the resulting graph provides several interactive options to evaluate results. The screenshot below provides the output of the single computing mode of CAST.

Image chu2004_2:

### Dynamically comparing model results - using sliders

Sliders are activated once the **`Generate Graph`** is clicked (see Interactive options in the Single computing interface). Sliders are provided for more critical model parameters that have been suggested in Chu et al. (2004) paper. Sliders changes the model input parameters; for which the output $L_{max}$ appears in the graph. This enables a dynamic computation and visualization. 

### Multiple computing interface

The multiple computing interface of the Chu et al. (2004) model is identical to [Liedl et al. (2005)](refli2005) model interface. The goal of the multiple computing interface  is to develop several scenarios and compare the output of these scenarios with that of the field data. As can be observed in the screenshot below, users have an option to select the site(s) they would like to compare their scenarios with.

Image chu2004_3:

The interface of multiple computing interface is provided in the screenshot below. Details on the options are identical to that provided for [Liedl et al. (2005)](refli2005) model that is provided [here](refli).

Image chu2004_4:

