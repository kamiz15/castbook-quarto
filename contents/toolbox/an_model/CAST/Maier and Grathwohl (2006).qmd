### Maier and Grathwohl (2006)

This 2D model provides an estimate of a steady-state plume length ($L_{max}$) and analyses the sensitivity of the plume length with respect to biodegradation kinetics, flow velocity, transverse vertical dispersivity, the source and aquifer geometry and reaction stoichiometry.

Maier and Grathwohl (2005) provides the following explicit expression for $L_{max}$ :
$$
L_{max} = 0.5\frac{M^2}{\alpha_{TV}}\bigg(\frac{\gamma C_{ED}}{C_{EA}}\bigg)^{0.3}
$$
$M$ = Source Length [L]
$\alpha_{TV}$ = Vertical Transverse Dispersivity [L]
$\gamma$ = Reaction stoichiometric ratio [ ]
$C_{ED}$ = Contaminant (Electron Donor) concentration [ML$^{-3}$]
$C_{EA}$ = Partner Reactant (Electron Acceptor) concentration [ML$^{-3}$]

**The model is based on the following assumptions:**

1. A uniform flow field in an aquifer of constant thickness is assumed.
2. A completely contaminated aquifer thickness (landfill or boundary source) is presumed.

#### Reference:

 U.Maier , P.Grathwohl 2005 . Numerical experiments and field results on the size of steady state plumes. https://doi.org/10.1016/j.jconhyd.2005.12.012

### Using Maier and Grathwohl (2006) model in CAST

### Single computing interface

The CAST user-interface for Both the empirical models are identical. This is true for both single computing interface and multiple simulation interface. The identical interface simplifies the use of models in the CAST. Therefore, the extensive details on using the  [Liedl et al. (2005)](refli2005)  model in CAST provided [here](refli) can be used also for the Maier and Grathwohl (2006).

The difference in each model interface is the model specific parameters. This can be observed in the CAST screenshot below: 

Image MG_1:

Once the input data is placed in the box, user needs to click on the **`Generate Graph`** to get the result. Results are obtained as an absolute number below the Generate Graph button and also graphically, which provides the field plume length data from the database. This allows a visual comparison of the model $L_{max}$with the field data.



As explained in detail in [Liedl et al. (2005)](refli2005)  model , the resulting graph provides several interactive options to evaluate results. The screenshot below provides the output of the single computing mode of CAST.

Image:

### Dynamically comparing model results - using sliders

Sliders are activated once the **`Generate Graph`** is clicked (see Interactive options in the Single computing interface). Sliders are provided for more critical model parameters that have been suggested in Maier and Grathwohl (2006) paper. Sliders changes the model input parameters; for which the output $L_{max}$ appears in the graph. This enables a dynamic computation and visualization. 

### Multiple computing interface

The multiple computing interface of the Chu et al. (2004) model is identical to analytical model  [Liedl et al. (2005)](refli2005) model interface. The goal of the multiple computing interface  is to develop several scenarios and compare the output of these scenarios with that of the field data. As can be observed in the screenshot below, users have an option to select the site(s) they would like to compare their scenarios with.

Image:

The interface of multiple computing interface is provided in the screenshot below. Details on the options are identical to that provided for [Liedl et al. (2005)](refli2005)  model that is provided [here](refli).

Image