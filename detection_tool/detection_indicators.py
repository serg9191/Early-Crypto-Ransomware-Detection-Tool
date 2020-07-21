class DetectionIndicators():
  """
  A class used to record states of vialations
  and associated actions

  Attributes
  ---
  entropy_violation: boolean
    A boolean containing state of entropy violation
  file_type_change: boolean
    A boolean containing state of file type change
  similarity_violation: boolean
    A boolean containing state of similarity violation
  evaluation_score: int
    An integer recording number of violation indicators  

  Methods
  ---
  excessive_entropy()
    changes the state of entropy_violation variable to true
  file_type_changed()
    changes the state of file_type_changed variable to true
  dissimilar_hash(url)
    changes the state of similarity_violation variable to true
  detection_evaluation_score()
    the mothod that produces numeric score of triggered
    detection indicators by iteratig all class fields except one
  associate_score_with_descriptor()
    the mothad that associates identified numeric indicator
    with the descriptor
  """      
  def __init__(self, entropy_violation = False,
      file_type_change = False, similarity_violation = False,
      evaluation_score = 0):
    """
    Parameters
    ----------
    entropy_violation : boolean
      entropy violation state
    file_type_change : boolean
      file type change state
    similarity_violation : boolean
      similarity violation state
    evaluation_score : int
      numeric representation of how many
      indicators/violations were triggered
    """     

    self.entropy_violation = entropy_violation
    self.file_type_change = file_type_change
    self.similarity_violation = similarity_violation
    self.evaluation_score = evaluation_score

  # This method changes state of entropy_violation field to True
  def excessive_entropy(self):
    self.entropy_violation = True
  # This method changes state of file_type_change field to True
  def file_type_changed(self):
    self.file_type_change = True
  # This method changes state of similarity_violation field to True
  def dissimilar_hash(self):
    self.similarity_violation = True

  # This method calculates number of indicators/violations
  # triggered and returns numeric value, score
  def detection_evaluation_score(self):
    # Iterate all class fields. Filtering added to exclude
    # methods and instances and evaluation_score field
    indicators = [
      field for field in dir(DetectionIndicators())
      if not callable(getattr(DetectionIndicators(), field))
      and field != "evaluation_score"
      and not field.startswith("__")
    ]

    self.evaluation_score = 0

    # calculate number of indicators triggered
    for indicator in indicators:
      if getattr(self, indicator) == True:
        self.evaluation_score += 1

    # Return score numeric score via
    # associate_score_with_descriptor method 
    return self.associate_score_with_descriptor()

  # This method associates numeric values of score with the
  # actual descriptor
  def associate_score_with_descriptor(self):
    # Associate one of four possible numeric values with
    # the descriptor and return tuple obj(score, descriptor)
    if self.evaluation_score == 1:
      return(self.evaluation_score, "unlikely")

    if self.evaluation_score == 2:
      return(self.evaluation_score, "possibly")

    if self.evaluation_score == 3:
      return(self.evaluation_score, "ransomware detected")

    return(self.evaluation_score, "no ransomware detected")


