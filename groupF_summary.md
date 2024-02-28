Types of diagnoses and how they relate

After viewing the description for the given dataset, we can be sure that we are presented with skin lesions such as: Basal Cell Carcinoma (BCC), Squamous Cell Carcinoma (SCC), Actinic Keratosis (ACK), Seborrheic Keratosis (SEK), Bowen’s disease (BOD), Melanoma (MEL), and Nevus (NEV).  These skin lesions are also divided into two groups: skin cancers (BCC, MEL, SCC(including BOD)), skin diseases (ACK, SEK, and NEV).  In addition, we may note that MEL, NEV, and SEK are pigmented skin lesions and SCC, BCC and ACK are non-pigmented ones.1

BCC also known as Basal Cell Carcinoma, is a skin cancer type, which is one of the most common ones among different skin cancer types. In the data set there are a total of 845 instances of the BCC diagnoses, making it the most common one in the dataset.2 It generally contains features like bleeding, pain and present elevation. Features that are shared by the SCC skin cancer type, making it difficult to distinguish the two types based on those features.3

MEL or Melanoma is the deadliest type of skin cancer. Melanoma is a molecularly heterogeneous disease, with diverse genomic alterations and clinical phenotypes. Some mutations are well characterized, but the significance of others remains unclear. Often melanoma has no symptoms, however, the first sign is generally a change in an existing mole or the appearance of a new spot.4

SCC or as it is also known as Squamous Cell Carcinoma, is one of the most common skin cancers in the world.5 Common symptoms for SCC are tenderness and change in size for the lesion.6 There are a total of 192 people from the data set that have been diagnosed with SCC.2

Common symptoms of SEK are scaling, itching and erythema.7 It typically appears in the face.4 In the data set it accounts for 235 images of the total 2298 images.2

Missing data and low quality images.

Since there is a lot of missing data in the table provided to us, we were forced to clean it up.
When cleaning the data based on the columns “gender information”, “skin cancer history”, “cancer history”, 
“region”, “diagnostic” and “image id” we got a total of 804 rows where one of the before mentioned columns has NaN as its input. In our further research, we used data without this 804 rows, to draw conclusions.

No column in the data set shows whether or not the picture is of low quality, so there might be some pictures we can't use but since that data set after cleaning is 1494 
and that is too many pictures to go through one by one. Working with the data set description, we can be sure that the pictures are of different sizes and most likely of different quality, since they were made by different devices. Low-quality photos can affect masks, and accordingly they can affect the result of our research.

Prevalence of the different skin cancers and diseases:

For this part we have used our cleaned version of the dataset (Without all the null values)
We have 741 Males and 753 Females in the study, so 1494 people in total.
We can from our data deepdive see the following split between genders:

BCC: Males 439 (59.23%), Females 406 (53.91%), Both genders 845 (56.55%)

ACK: Males 130 (17.54%), Females 153 (20.31%), Both genders 283 (18.94%)

SCC: Males 102 (13.76%), Females 90  (11.95%), Both genders 192 (12.85%)

NEV: Males 26  ( 3.50%), Females 49  ( 6.50%), Both genders 75  ( 5.02%)

MEL: Males 24  ( 3.23%), Females 28  ( 3.71%), Both genders 52  ( 3.48%)

SEK: Males 20  ( 2.69%), Females 27  ( 3.58%), Both genders 47  ( 3.14%)

From these statistics we can see a significant difference in the prevalence of Nevus, there are almost 2 females with the skin disease for 1 man with the skin disease. 
This might indicate some sort of weakness for this specific disease in Females. 
There is also a difference in Actinic Keratosis for males and females, here there is 17.54% prevalence for males and 20.31% prevalence for females. 
There is a difference in the prevalence of Basal Cell Carcinoma, here the prevalence for males is 59.23% while it is 56.55% for females. 
Finally for Seborrheic Keratosis the difference in prevalence is  2.69% for males and 3.58% for females, which is a quite big difference.

Citations:

1: https://data.mendeley.com/datasets/zr7vgbcyr2/1

2: Metadata_deepdive.py in our repository

3: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4143108/

4: https://www.sciencedirect.com/science/article/pii/S0010482519304019#tbl1

5: https://doi.org/10.1007/978-1-4612-3790-7_5

6: https://doi.org/10.1016/j.jaad.2006.11.032.
(https://www.sciencedirect.com/science/article/pii/S0190962206040965)

7: https://www.aafp.org/pubs/afp/issues/2015/0201/p185.html?adb_sid=3f2fa233-444b-4e87-a5c4-0277499c4be4 
